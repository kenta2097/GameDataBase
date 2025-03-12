import os
import yaml
import pandas as pd
import time
import argparse
import sys
import platform
from colorama import init, Fore, Style, AnsiToWin32

# Initialize colorama for Windows support
if platform.system() == 'Windows':
    init(wrap=False)
    import sys
    sys.stdout = AnsiToWin32(sys.stdout)
else:
    init()

# Simplified argument processing
parser = argparse.ArgumentParser(description='Tag Guardian - Validate game tags in CSV files')
parser.add_argument('files', nargs='*', 
    help='CSV files to process. If none provided, all CSV files will be processed')
parser.add_argument('--output', type=str, 
    help='Output path for the report (default: tag_guardian_report.md)')

# Report sections control
report_group = parser.add_argument_group('Report sections')
report_group.add_argument('--no-stats', action='store_true', help='Hide Games and Tags statistics')
report_group.add_argument('--no-overview', action='store_true', help='Hide Overview section')
report_group.add_argument('--no-validation', action='store_true', help='Hide Validation Results')
report_group.add_argument('--no-actions', action='store_true', help='Hide Suggested Actions')
report_group.add_argument('--no-unregistered', action='store_true', help='Hide Unregistered Tags')
report_group.add_argument('--no-errors', action='store_true', help='Hide Invalid Tags Found')
report_group.add_argument('--no-warnings', action='store_true', help='Hide Warnings section')
report_group.add_argument('--compact', action='store_true', help='Show only Essential sections')

# Load tags.yml
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

with open(os.path.join(root_dir, 'tags.yml'), 'r') as file:
    tags_definitions = yaml.safe_load(file)
print("Loaded tags.yml")

# Function to validate tags
def validate_tags(tags_str, tags_definitions):
    """Validate tags for a single game"""
    errors = []
    warnings = []
    valid_count = 0
    total_tags = 0
    
    if not isinstance(tags_str, str):
        return [], warnings, 0, 0
    
    # Get all tags and check for basic warnings
    individual_tags = [t.strip() for t in tags_str.split() if t.strip()]
    tag_set = set(individual_tags)
    
    # 1. Essential validations
    essential_tags = ['#genre', '#players']
    missing_essential = [tag for tag in essential_tags if not any(t.startswith(tag) for t in tag_set)]
    if missing_essential:
        warnings.append(f"Missing essential tags: {', '.join(missing_essential)}")
    
    # 2. Language and region validations
    if any('@' in tag and ('デ' in tag or 'ド' in tag or 'ー' in tag) for tag in tag_set):
        if not any(t.startswith('#lang:ja') for t in tag_set):
            warnings.append("Game appears to be Japanese but missing #lang:ja tag")
    
    # 3. Specific hardware validations
    hardware_pairs = {
        'randnetmodem': '64dd',  # If has randnetmodem should have 64dd
        'capturecassette': '64dd',  # If has capture cassette should have 64dd
        'n64mic': '64dd',  # If has N64 mic should have 64dd
    }
    
    addon_tags = [t for t in tag_set if t.startswith('#addon:')]
    for addon in addon_tags:
        for req_hw, dep_hw in hardware_pairs.items():
            if req_hw in addon and not any(dep_hw in t for t in addon_tags):
                warnings.append(f"Game uses {req_hw} but {dep_hw} may be required")
    
    # 4. Player validations
    player_tags = [t for t in tag_set if t.startswith('#players:')]
    for ptag in player_tags:
        if ':vs' in ptag and not any(f'players:{n}' in t for t in tag_set for n in ['2','3','4']):
            warnings.append("Game marked as versus but player count not specified")
        if ':coop' in ptag and not any(f'players:{n}' in t for t in tag_set for n in ['2','3','4']):
            warnings.append("Game marked as cooperative but player count not specified")
    
    # 5. Genre validations
    genre_tags = [t for t in tag_set if t.startswith('#genre:')]
    if len(genre_tags) > 3:
        warnings.append("Too many genre tags (more than 3)")
    
    # 6. Status and version validations
    if any('unfinished:' in tag for tag in tag_set):
        if not any(status in tag for tag in tag_set for status in ['beta', 'proto', 'demo']):
            warnings.append("Game marked as unfinished but specific status not provided")
    
    # 7. Franchise validations
    franchise_refs = [t for t in tag_set if t.startswith('$')]
    if franchise_refs and not any(t.startswith('#franchise:') for t in tag_set):
        warnings.append("Game has franchise reference ($) but missing #franchise tag")

    # 8. Special devices validations
    special_devices = {
        'lightphaser': 'shooting',  # Light phaser should have shooting genre
        'menacer': 'shooting',      # Menacer should have shooting genre
        'justifier': 'shooting',    # Justifier should have shooting genre
        'zapper': 'shooting'        # Zapper should have shooting genre
    }
    
    for device in special_devices.keys():
        if any(device in t for t in addon_tags):
            if not any(special_devices[device] in t for t in genre_tags):
                warnings.append(f"Game uses {device} but genre:{special_devices[device]} not specified")

    # Rest of tag validation
    tag_errors = []
    
    for tag in individual_tags:
        if not tag.startswith('#'):
            continue
            
        total_tags += 1
        current_tag_errors = []
        
        # Split by '>' first to handle third level
        parts = tag[1:].split('>')  # Remove # and split
        if len(parts) > 2:
            current_tag_errors.append((f"Too many '>' separators in tag: '{tag}'", None))
            continue

        base_parts = parts[0].split(':')
        value = parts[1] if len(parts) == 2 else None

        # Handle different levels
        if len(base_parts) == 1:
            category = base_parts[0]
            # Check if it's a standalone tag
            if category in tags_definitions.get('standalone', {}).get('values', {}):
                if value:  # Standalone tags shouldn't have a value
                    current_tag_errors.append((f"Standalone tag '{category}' cannot have a value", None))
                
            # Check if it's a valid main category
            elif category not in tags_definitions:
                current_tag_errors.append((f"Unknown category: '{category}'", None))

        elif len(base_parts) == 2:
            category, subcategory = base_parts
            
            # Validate category exists
            if category not in tags_definitions:
                current_tag_errors.append((f"Unknown category: '{category}'", None))
                continue

            # Check if category is of type nested
            category_type = tags_definitions[category].get('type')
            if category_type == 'nested':
                # For nested types, subcategory should be in subcategories
                if subcategory not in tags_definitions[category].get('subcategories', {}):
                    current_tag_errors.append((f"Invalid subcategory: '{subcategory}' for nested category '{category}'", None))
                # Nested types don't have values
                if value:
                    current_tag_errors.append((f"Nested category '{category}:{subcategory}' cannot have a value", None))
            else:
                # For non-nested types, validate subcategory and value normally
                if subcategory not in tags_definitions[category].get('subcategories', {}):
                    current_tag_errors.append((f"Unknown subcategory: '{subcategory}' in '{category}'", None))
                    continue

                # Validate value if present
                if value:
                    valid_values = tags_definitions[category]['subcategories'][subcategory].get('values', {})
                    if value not in valid_values:
                        current_tag_errors.append((f"Invalid value: '{value}' for '{category}:{subcategory}'", None))
        else:
            current_tag_errors.append((f"Invalid tag format: '{tag}'", None))
        
        if current_tag_errors:
            tag_errors.append((tag, current_tag_errors))
        else:
            valid_count += 1

    return tag_errors, warnings, valid_count, total_tags

def get_csv_files(root_dir: str, specified_files: list = None) -> list:
    """Get list of CSV files to process"""
    csv_files = []
    
    # If no files specified, search recursively in all directories
    if not specified_files:
        for root, _, files in os.walk(root_dir):
            # Skip scripts directory using platform-independent path split
            if 'scripts' in root.split(os.path.sep):
                continue
            csv_files.extend(os.path.join(root, f) for f in files if f.endswith('.csv'))
    else:
        csv_files = [os.path.abspath(f) for f in specified_files if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in", root_dir)
        sys.exit(1)
        
    print(f"\nFound {Fore.CYAN}{len(csv_files)}{Style.RESET_ALL} CSV files to process:")
    for f in csv_files:
        # Use os.path.relpath for cross-platform path display
        print(f"  - {Fore.BLUE}{os.path.relpath(f, root_dir)}{Style.RESET_ALL}")
    print()
    
    return sorted(csv_files)

def process_csv_file(file_path: str, tags_definitions: dict) -> tuple:
    """Process single CSV file and return results"""    
    print(f"Processing file: {os.path.basename(file_path)}")
    df = pd.read_csv(file_path)
    
    if 'Tags' not in df.columns:
        print(f"Skipping file (no 'Tags' column): {os.path.basename(file_path)}")
        return None
        
    file_result = {
        'file': os.path.basename(file_path),
        'valid': 0, 'total': 0, 'invalid': 0, 'warnings': 0
    }
    
    file_errors = []
    file_warnings = []
    games_processed = {}
    
    for idx, row in df.iterrows():
        results = process_game_row(row, idx, file_path, tags_definitions)
        if results:
            game_stats, errors, warnings = results
            update_file_stats(file_result, game_stats)
            file_errors.extend(errors)
            file_warnings.extend(warnings)
            games_processed.update(game_stats['games'])
            
    return file_result, file_errors, file_warnings, games_processed

def process_game_row(row: pd.Series, idx: int, file_path: str, tags_definitions: dict) -> tuple:
    """Process single game row and return results"""
    game_title = row['Screen title @ Exact'] if 'Screen title @ Exact' in row else 'Unknown'
    
    # Create internal row tracking without showing it in reports
    internal_id = f"{game_title}__row_{idx + 1}"  # Double underscore to avoid conflicts
    display_id = game_title  # Only show game title in reports
    
    tags_str = row['Tags']
    tag_errors, warnings, valid_count, total_tags = validate_tags(tags_str, tags_definitions)
    
    game_stats = {
        'games': {
            internal_id: {
                'has_errors': bool(tag_errors),
                'has_warnings': bool(warnings),
                'total_tags': total_tags,
                'valid_tags': valid_count,
                'processed': True,
                'original_title': game_title,
                'display_title': display_id,
                'row': idx + 1,  # Keep row number for internal reference
                'warnings_count': len(warnings)
            }
        }
    }
    
    errors = []
    if tag_errors:
        errors.append({
            'file': os.path.basename(file_path),
            'row': idx + 1,
            'game': display_id,  # Use clean title for display
            'internal_id': internal_id,  # Keep internal reference
            'original_title': game_title,
            'tag_errors': tag_errors
        })
    
    game_warnings = []
    if warnings:
        game_warnings.append({
            'file': os.path.basename(file_path),
            'row': idx + 1,
            'game': display_id,  # Use clean title for display
            'internal_id': internal_id,  # Keep internal reference
            'original_title': game_title,
            'tag': tags_str,
            'warning': warnings
        })
        
    return game_stats, errors, game_warnings

def update_file_stats(file_result: dict, game_stats: dict):
    """Update file statistics with game statistics"""
    for game, stats in game_stats['games'].items():
        file_result['valid'] += stats['valid_tags']
        file_result['total'] += stats['total_tags']
        file_result['invalid'] = file_result['total'] - file_result['valid']
        # Accumulate warnings instead of overwriting
        file_result['warnings'] += stats['warnings_count']

def generate_markdown_report(stats: dict, file_results: list, file_path: str, args):
    """Generate markdown report with given statistics based on command line arguments"""
    # Clean up previous reports using platform-independent paths
    reports_dir = os.path.join(os.path.dirname(file_path), 'reports')
    
    # Remove old report file if exists
    if os.path.exists(file_path):
        print(f"{Fore.YELLOW}Removing old report:{Style.RESET_ALL} {file_path}")
        os.remove(file_path)
        
    # Remove old reports directory and its contents
    if os.path.exists(reports_dir):
        print(f"{Fore.YELLOW}Removing old reports directory:{Style.RESET_ALL} {reports_dir}")
        import shutil
        try:
            shutil.rmtree(reports_dir)
        except PermissionError:
            print(f"{Fore.RED}Error removing reports directory. Please close any open files.{Style.RESET_ALL}")
            sys.exit(1)
    
    # Create fresh reports directory
    print(f"{Fore.GREEN}Creating reports directory:{Style.RESET_ALL} {reports_dir}")
    os.makedirs(reports_dir, exist_ok=True)
    
    # Generate new reports
    with open(file_path, 'w') as report_file:
        # Write header and basic sections
        write_main_report(report_file, stats, file_results, args)
        
        # List of detailed reports
        if not args.no_errors or not args.no_warnings:
            write_detailed_reports_index(report_file, stats, file_results)
            
        # Generate individual reports by file
        for file_result in file_results:
            generate_file_reports(stats, file_result, reports_dir)

def write_detailed_reports_index(report_file, stats, file_results):
    """Write index of detailed reports with links"""
    report_file.write("\n## 📑 Detailed Reports by File\n\n")
    
    # List of error reports
    report_file.write("### ❌ Invalid Tags Reports\n")
    for file_result in file_results:
        file_errors = [e for e in stats['errors'] if e['file'] == file_result['file']]
        if file_errors:
            csv_name = os.path.splitext(file_result['file'])[0]
            report_file.write(f"- [📋 {file_result['file']} ({len(file_errors)} errors)](reports/{csv_name}_errors.md)\n")
    report_file.write("\n")
    
    # List of warning reports
    report_file.write("### ⚠️ Warning Reports\n")
    for file_result in file_results:
        file_warnings = [w for w in stats['warnings'] if w['file'] == file_result['file']]
        if file_warnings:
            csv_name = os.path.splitext(file_result['file'])[0]
            report_file.write(f"- [📋 {file_result['file']} ({len(file_warnings)} warnings)](reports/{csv_name}_warnings.md)\n")
    report_file.write("\n")

def write_main_report(report_file, stats, file_results, args):
    """Write main sections of the report"""
    report_file.write("# 📊 Tag Guardian Report\n\n")
    
    if not args.no_stats and not args.compact:
        write_header_stats(report_file, stats)
        
    if not args.no_overview and not args.compact:
        write_overview_section(report_file, stats)
        
    if not args.no_validation:
        write_validation_results(report_file, file_results)
        
    if not args.no_unregistered and not args.compact and stats['unregistered_tags']:
        write_unregistered_tags(report_file, stats['unregistered_tags'])
    
    if not args.no_actions and not args.compact:
        write_suggested_actions(report_file)

def generate_file_reports(stats: dict, file_result: dict, reports_dir: str):
    """Generate separate error and warning reports for each CSV file"""
    csv_name = os.path.splitext(file_result['file'])[0]
    
    # Generate errors reports
    file_errors = [e for e in stats['errors'] if e['file'] == file_result['file']]
    if file_errors:
        error_path = os.path.join(reports_dir, f"{csv_name}_errors.md")
        with open(error_path, 'w') as error_file:
            error_file.write(f"# ❌ Invalid Tags Report - {file_result['file']}\n\n")
            write_error_section(error_file, file_errors, [file_result])
    
    # Generate warnings reports
    file_warnings = [w for w in stats['warnings'] if w['file'] == file_result['file']]
    if file_warnings:
        warning_path = os.path.join(reports_dir, f"{csv_name}_warnings.md")
        with open(warning_path, 'w') as warning_file:
            warning_file.write(f"# ⚠️ Warnings Report - {file_result['file']}\n\n")
            write_warning_section(warning_file, file_warnings, [file_result])

def generate_errors_report(errors: list, file_results: list):
    """Generate separate report for invalid tags"""
    with open('tag_guardian_errors.md', 'w') as report_file:
        report_file.write("# ❌ Invalid Tags Report\n\n")
        write_error_section(report_file, errors, file_results)

def generate_warnings_report(warnings: list, file_results: list):
    """Generate separate report for warnings"""
    with open('tag_guardian_warnings.md', 'w') as report_file:
        report_file.write("# ⚠️ Warnings Report\n\n")
        write_warning_section(report_file, warnings, file_results)

def load_tag_definitions(root_dir: str) -> dict:
    """Load tag definitions from tags.yml"""
    with open(os.path.join(root_dir, 'tags.yml'), 'r') as file:
        return yaml.safe_load(file)

def calculate_statistics(results: list) -> dict:
    """Calculate overall statistics from results"""
    stats = {
        'total_tags': 0,
        'valid_tags': 0,
        'invalid_tags': 0,
        'warnings_count': 0,
        'total_games': 0,
        'valid_games': 0,
        'games_with_errors': 0,
        'games_with_warnings': 0,
        'errors': [],
        'warnings': [],
        'unregistered_tags': [],
        'games_list': {
            'valid': [],
            'invalid': [],
            'warnings': []
        },
        'files_processed': len([r for r in results if r[0] is not None])  # Count only processed files
    }
    
    processed_games = {}
    for result in results:
        file_result, file_errors, file_warnings, games_processed = result
        stats['total_tags'] += file_result['total']
        stats['valid_tags'] += file_result['valid']
        stats['invalid_tags'] += file_result['invalid']
        stats['warnings_count'] += sum(len(w['warning']) for w in file_warnings)  # Corregir conteo de warnings
        stats['errors'].extend(file_errors)
        stats['warnings'].extend(file_warnings)
        processed_games.update(games_processed)
    
    stats['total_games'] = len(processed_games)
    stats['valid_games'] = sum(1 for status in processed_games.values() 
                             if not status['has_errors'] and not status['has_warnings'])
    stats['games_with_errors'] = sum(1 for status in processed_games.values() 
                                   if status['has_errors'])
    stats['games_with_warnings'] = sum(1 for status in processed_games.values() 
                                     if status['has_warnings'])
    stats['unregistered_tags'] = collect_unregistered_tags(stats['errors'])
    
    # Collect valid, invalid, and warning games
    for game, status in processed_games.items():
        if status['has_errors']:
            stats['games_list']['invalid'].append(game)
        elif status['has_warnings']:
            stats['games_list']['warnings'].append(game)
        else:
            stats['games_list']['valid'].append(game)
    
    return stats

def collect_unregistered_tags(all_errors):
    # Count occurrences of unregistered tags
    tag_counts = {}
    for error in all_errors:
        if error['tag_errors'][0][1][0][0].startswith('Unknown category'):
            # Split compound tags
            tags = error['tag_errors'][0][0].split()
            for single_tag in tags:
                tag_counts[single_tag] = tag_counts.get(single_tag, 0) + 1
    
    # Generate suggestions based on tag patterns
    tag_suggestions = {}
    common_categories = {
        'players': 'Add player count category with numeric values',
        'save': 'Add save feature category (backup, memory, etc)',
        'lang': 'Add language support category (en, ja, etc)',
        'region': 'Add region category (jp, us, eu, etc)',
        'mode': 'Add game mode category (vs, coop, etc)'
    }
    
    for tag in tag_counts:
        category = tag.split(':')[0] if ':' in tag else tag
        category = category.replace('#', '')
        if category in common_categories:
            tag_suggestions[tag] = common_categories[category]
        else:
            tag_suggestions[tag] = f"Consider adding {category} category"
    
    return [(tag, count, tag_suggestions[tag]) 
            for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)]

def write_header_stats(report_file, stats):
    """Write header statistics to report file"""
    # Column headers común para ambas tablas
    header_format = "|  📊 Metric | 🔢 Count | 📈 % | 🚦 Status | 📝 Details |\n"
    separator = "|------------|-----------|-------|-----------|------------|\n"

    # Games Statistics
    report_file.write("### 🎮 Games Stats\n")
    report_file.write(header_format)
    report_file.write(separator)
    report_file.write(f"| ✅ Valid Games | **{stats['valid_games']}** | `{stats['valid_games']/stats['total_games']*100:.1f}%` | 🟢 | No issues found |\n")
    report_file.write(f"| ❌ Invalid Games | **{stats['games_with_errors']}** | `{stats['games_with_errors']/stats['total_games']*100:.1f}%` | 🔴 | Need fixes |\n")
    report_file.write(f"| ⚠️ Warning Games | **{stats['games_with_warnings']}** | `{stats['games_with_warnings']/stats['total_games']*100:.1f}%` | 🟡 | Review suggested |\n")
    report_file.write(f"| 🎲 Total Processed | **{stats['total_games']}** | `100%` | ⚪ | Unique entries |\n\n")
    
    # Tags Statistics  
    report_file.write("### 🏷️ Tags Stats\n")
    report_file.write(header_format)
    report_file.write(separator)
    report_file.write(f"| ✅ Valid Tags | **{stats['valid_tags']}** | `{stats['valid_tags']/stats['total_tags']*100:.1f}%` | 🟢 | Correct format |\n")
    report_file.write(f"| ❌ Invalid Tags | **{stats['invalid_tags']}** | `{stats['invalid_tags']/stats['total_tags']*100:.1f}%` | 🔴 | Format errors |\n") 
    report_file.write(f"| ⚠️ Warning Tags | **{stats['warnings_count']}** | `{stats['warnings_count']/stats['total_tags']*100:.1f}%` | 🟡 | Need review |\n")
    report_file.write(f"| 📝 Total Tags | **{stats['total_tags']}** | `100%` | ⚪ | All entries |\n\n")

def write_overview_section(report_file, stats):
    """Write overview section to report file"""
    report_file.write("## 📈 Overview\n\n")
    
    # Processing Statistics
    report_file.write("### 🔄 Processing Stats\n")
    report_file.write("| Metric | Value | Details |\n")
    report_file.write("|--------|--------|----------|\n")
    # Use length of results list instead of errors
    report_file.write(f"| Files Processed | {stats['files_processed']} | 📁 Total CSV files analyzed |\n")
    report_file.write(f"| Processing Time | {stats['processing_time']:.2f}s | ⏱️ Total execution time |\n\n")

def write_validation_results(report_file, file_results):
    """Write validation results to report file"""
    report_file.write("### 📊 Validation Results\n")
    report_file.write("_Note: Total Tags are the non-unique Individual tags in each file_\n\n")
    report_file.write("| 📁 File | ✅ Valid | ❌ Invalid | ⚠️ Warnings | 📝 Total |\n")
    report_file.write("|---------|-----------|------------|-------------|----------|\n")
    for result in file_results:
        report_file.write(f"| `{result['file']}` | **{result['valid']}** | **{result['invalid']}** | **{result['warnings']}** | {result['total']} |\n")

def write_suggested_actions(report_file):
    """Write suggested actions to report file"""
    # Main section with key points
    report_file.write("\n## 🎯 Suggested Actions\n\n")
    report_file.write("1. 🔍 Review and fix invalid tags\n")
    report_file.write("2. ⭐ Ensure essential tags are present\n")
    report_file.write("3. 🌏 Check regional content tags\n")
    report_file.write("4. 🎮 Verify hardware compatibility\n\n")
    
    # Collapsible detailed section
    report_file.write("<details>\n")
    report_file.write("<summary>📚 More details</summary>\n\n")
    
    # Fix Invalid Tags
    report_file.write("### ❌ Fix Invalid Tags\n")
    report_file.write("1. 🔄 Check and correct tag format:\n")
    report_file.write("   - Use `#category:subcategory>value` format\n")
    report_file.write("   - Example: `#genre:sports>football`\n")
    report_file.write("2. 🎯 Verify tags against tags.yml:\n")
    report_file.write("   - All categories must be defined\n")
    report_file.write("   - All subcategories must exist\n")
    report_file.write("   - Values must match allowed options\n\n")
    
    # Essential Tags
    report_file.write("### ⭐ Add Essential Tags\n")
    report_file.write("1. Required for all games:\n")
    report_file.write("   - `#genre:` - Main game genre\n")
    report_file.write("   - `#players:` - Number of players\n\n")
    
    # Common Categories
    report_file.write("### 🏷️ Common Tag Categories\n")
    report_file.write("| Category | Description | Example |\n")
    report_file.write("|----------|-------------|----------|\n")
    report_file.write("| `#genre:` | Game genre classification | `#genre:action` |\n")
    report_file.write("| `#players:` | Player count & modes | `#players:2:vs` |\n")
    report_file.write("| `#addon:` | Required peripherals | `#addon:lightgun` |\n")
    report_file.write("| `#lang:` | Game language | `#lang:ja` |\n")
    report_file.write("| `#save:` | Save functionality | `#save:backup` |\n")
    report_file.write("| `#franchise:` | Game franchise | `#franchise:mario` |\n")
    report_file.write("| `#official:` | Official content | `#official:sports` |\n")
    report_file.write("| `#mode:` | Game mode | `#mode:story` |\n")
    report_file.write("| `#status:` | Game status | `#status:proto` |\n")
    report_file.write("| `#input:` | Input method | `#input:joystick` |\n\n")

    # Hardware Related Tags
    report_file.write("### 🎮 Hardware Related Tags\n")
    report_file.write("1. Required peripherals:\n")
    report_file.write("   - Use `#addon:` for hardware requirements\n")
    report_file.write("   - Example: `#addon:64dd:expasionpak:mouse>n64`\n")
    report_file.write("2. Hardware dependencies:\n")
    report_file.write("   - Some addons require other hardware\n")
    report_file.write("   - Example: randnetmodem requires 64dd\n\n")

    # Regional Content
    report_file.write("### 🌏 Regional Content\n")
    report_file.write("1. Language tags:\n")
    report_file.write("   - Use `#lang:` for game text language\n")
    report_file.write("   - Japanese games must include `#lang:ja`\n")
    report_file.write("2. Region-specific content:\n")
    report_file.write("   - Check title in different regions\n")
    report_file.write("   - Verify hardware compatibility\n\n")

    # Special Cases
    report_file.write("### 🔍 Special Cases\n")
    report_file.write("1. Franchise references:\n")
    report_file.write("   - Use `$` for franchise references\n")
    report_file.write("   - Add corresponding `#franchise:` tag\n")
    report_file.write("2. Game status:\n")
    report_file.write("   - Mark unfinished games (beta, proto, demo)\n")
    report_file.write("   - Add revision info if needed\n\n")
    
    # Documentation
    report_file.write("### 📚 Documentation\n")
    report_file.write("1. Tags.yml reference:\n")
    report_file.write("   - Complete list of valid tags\n")
    report_file.write("   - Category descriptions\n")
    report_file.write("   - Allowed values and formats\n")
    report_file.write("2. Command options:\n")
    report_file.write("   - Use `--help` for more information\n")
    report_file.write("   - Check validation rules\n\n")
    
    # Close collapsible section
    report_file.write("</details>\n")

def write_unregistered_tags(report_file, unregistered_tags):
    """Write unregistered tags section to report file"""
    report_file.write("\n## Unregistered Tags\n")
    report_file.write("| Tag | Usage Count | Suggestion |\n")
    report_file.write("|-----|-------------|------------|\n")
    for tag, count, suggestion in unregistered_tags:
        report_file.write(f"| `{tag}` | {count} | {suggestion} |\n")

def write_error_section(report_file, errors, file_results):
    """Write error section to report file"""
    report_file.write("\n## ❌ Invalid Tags Found\n")
    
    # Determine if we need collapsible sections
    use_collapsible = len(file_results) > 1
    
    for file_result in file_results:
        file_errors = [error for error in errors if error['file'] == file_result['file']]
        if file_errors:
            if use_collapsible:
                report_file.write(f"\n<details>\n<summary>### 📄 {file_result['file']} ({len(file_errors)} errors)</summary>\n\n")
            else:
                report_file.write(f"\n### 📄 {file_result['file']}\n\n")
                
            report_file.write("| 🔢 Row | 🎮 Game | ❌ Invalid Tag | ℹ️ Error Types |\n")
            report_file.write("|--------|---------|---------------|---------------|\n")
            
            # Group errors by row and game
            grouped_errors = {}
            error_counts = {}  # Track number of errors per game
            
            # First pass: count errors per game
            for error in file_errors:
                game = error['game']
                if game not in error_counts:
                    error_counts[game] = 0
                error_counts[game] += len(error['tag_errors'])
            
            # Second pass: only group errors for games with invalid tags
            for error in file_errors:
                game = error['game']
                # Skip games where all tags are valid
                if error_counts[game] == 0:
                    continue
                    
                key = (error['row'], game)
                if key not in grouped_errors:
                    grouped_errors[key] = {'tags': [], 'messages': []}
                
                for tag, tag_errors in error['tag_errors']:
                    grouped_errors[key]['tags'].append(f'`{tag}`')
                    for e in tag_errors:
                        msg = e[0]
                        if msg.startswith("Unknown category:"):
                            category = msg.split("'")[1]
                            msg = f"Unknown category: '**{category}**'"
                        elif msg.startswith("Unknown subcategory:"):
                            subcategory = msg.split("'")[1]
                            msg = msg.replace(f"'{subcategory}'", f"'**{subcategory}**'")
                        elif msg.startswith("Invalid value:"):
                            value = msg.split("'")[1]
                            msg = msg.replace(f"'{value}'", f"'**{value}**'")
                        elif msg.startswith("Invalid tag format:"):
                            invalid_tag = msg.split("'")[1]
                            msg = f"Invalid tag format: '**{invalid_tag}**'"
                        elif msg.startswith("Standalone tag"):
                            tag = msg.split("'")[1]
                            msg = msg.replace(f"'{tag}'", f"'**{tag}**'")
                        grouped_errors[key]['messages'].append(msg)
            
            # Write grouped errors
            for (row, game), error_group in grouped_errors.items():
                if error_group['tags']:  # Only write if there are invalid tags
                    tags = '<br>'.join(error_group['tags'])
                    messages = '<br>'.join(error_group['messages'])
                    report_file.write(f"| {row} | {game} | {tags} | {messages} |\n")
            
            if use_collapsible:
                # Close details tag only if using collapsible
                report_file.write("\n</details>\n")

def write_warning_section(report_file, warnings, file_results):
    """Write warning section to report file"""
    report_file.write("\n## ⚠️ Warnings\n")
    
    # Determine if we need collapsible sections
    use_collapsible = len(file_results) > 1
    
    for file_result in file_results:
        file_warnings = [warning for warning in warnings if warning['file'] == file_result['file']]
        if file_warnings:
            if use_collapsible:
                report_file.write(f"\n<details>\n<summary>### 📄 {file_result['file']} ({len(file_warnings)} warnings)</summary>\n\n")
            else:
                report_file.write(f"\n### 📄 {file_result['file']}\n\n")
                
            report_file.write("| 🔢 Row | 🎮 Game | 🏷️ Tags | ⚠️ Warning |\n")
            report_file.write("|--------|---------|---------|------------|\n")
            for warning in file_warnings:
                # Split long tags into two lines if needed
                tags = warning['tag'].split()
                if len(tags) > 3:
                    tags_line1 = ' '.join(tags[:3])
                    tags_line2 = ' '.join(tags[3:])
                    tags_display = f"`{tags_line1}`<br>`{tags_line2}`"
                else:
                    tags_display = f"`{warning['tag']}`"
                
                report_file.write(f"| {warning['row']} | {warning['game']} | {tags_display} | {warning['warning']} |\n")
            
            if use_collapsible:
                # Close details tag only if using collapsible
                report_file.write("\n</details>\n")

def main():
    args = parser.parse_args()
    start_time = time.time()
    
    # Only show help if explicitly asked with -h/--help
    if '-h' in sys.argv or '--help' in sys.argv:
        print("\nTag Guardian - Validate tags in CSV files")
        print("\nExamples:")
        print("  Basic usage:")
        print("    python tag_guardian.py")
        print("    python tag_guardian.py file1.csv file2.csv")
        # ...existing help text...
        parser.print_help()
        sys.exit(0)
    
    # Load tags definitions from default location
    tags_definitions = load_tag_definitions(root_dir)
    
    # Process files - Pass None if no files specified to process all
    csv_files = get_csv_files(root_dir, args.files if args.files else None)
    results = [process_csv_file(f, tags_definitions) for f in csv_files if f]
    results = [r for r in results if r]
    
    # Generate report
    stats = calculate_statistics(results)
    stats['processing_time'] = time.time() - start_time
    
    report_path = args.output or os.path.join(root_dir, 'tag_guardian_report.md')
    generate_markdown_report(stats, [r[0] for r in results], report_path, args)
    
    print(f"{Fore.GREEN}\nProcessed {len(csv_files)} files{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Generated main report:{Style.RESET_ALL} {os.path.basename(report_path)}")
    print(f"{Fore.GREEN}Generated detail reports in:{Style.RESET_ALL} reports/")

if __name__ == '__main__':
    main()
