import React, { useEffect, useState } from 'react';
import yaml from 'js-yaml';
import './App.css';

interface TagValue {
  name?: string;
  capacities?: string[];
  manufacturer?: string;
}

interface SubValue {
  name?: string;
  capacities?: string[];
  manufacturer?: string;
}

interface TagData {
  type: string;
  description?: string;
  values?: Record<string, string | TagValue>;
  subcategories?: Record<string, {
    description?: string;
    values: Record<string, string | TagValue>;
  }>;
}

function App() {
  const [tagsData, setTagsData] = useState<Record<string, TagData>>({});
  const [selectedTags, setSelectedTags] = useState<Set<string>>(new Set());
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [selectedSubcategory, setSelectedSubcategory] = useState<string>('');

  useEffect(() => {
    // Changed for debugging load process
    fetch('/tags.yml')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
      })
      .then(text => {
        console.log('YAML text loaded:', text.substring(0, 100)); // Show first 100 characters
        const data = yaml.load(text) as Record<string, TagData>;
        console.log('Parsed data:', data);
        setTagsData(data);
      })
      .catch(error => {
        console.error('Detailed error:', error);
        alert('Error loading categories. Please check the console for details.');
      });
  }, []);

  const handleCategoryChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const category = event.target.value;
    setSelectedCategory(category);
    setSelectedSubcategory('');

    // If the category is simple and has no values, generate partial tag
    if (tagsData[category]?.type === 'simple' && 
        Object.keys(tagsData[category].values || {}).length === 0) {
      const partialTag = `${category}#`;
      
      setSelectedTags(prev => {
        const next = new Set(prev);
        Array.from(next).forEach(existingTag => {
          if (existingTag.startsWith(`${category}#`)) {
            next.delete(existingTag);
          }
        });
        next.add(partialTag);
        return next;
      });

      // Reset selections
      setSelectedCategory('');
    }
  };

  const formatTag = (category: string, subcategory: string | null, value: string, data: any): string => {
    // Special cases by category
    switch (category) {
      case 'franchise':
        return `#${category}>${value}`;
        
      case 'genre':
        if (!subcategory) return `#${category}:${value}`;
        if (!value) return `#${category}:${subcategory}`;
        return `#${category}:${subcategory}>${value}`;
        
      case 'input':
        if (subcategory && value) {
          return `#${category}:${subcategory}>${value}`;
        }
        return `#${category}:${subcategory}`;
        
      case 'format':
        if (typeof data === 'object' && data.capacities) {
          return `#${category}:${subcategory}>${value}`;
        }
        return `#${category}:${subcategory}>${value}`;
        
      default:
        // For simple categories
        if (currentCategory?.type === 'simple') {
          return `#${category}>${value}`;
        }
        // For nested categories with value
        if (subcategory && value) {
          return `#${category}:${subcategory}>${value}`;
        }
        // For nested categories without value
        return `#${category}:${subcategory}`;
    }
  };

  const handleSubcategoryChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const subcat = event.target.value;
    setSelectedSubcategory(subcat);
    
    // Generate tag immediately for categories that do not need value
    if (currentCategory?.type === 'nested' && 
        (!currentCategory.subcategories?.[subcat].values || 
         Object.keys(currentCategory.subcategories?.[subcat].values || {}).length === 0)) {
      const newTag = formatTag(selectedCategory, subcat, '', null);
      
      setSelectedTags(prev => {
        const next = new Set(prev);
        Array.from(next).forEach(existingTag => {
          if (existingTag.startsWith(`#${selectedCategory}`)) {
            next.delete(existingTag);
          }
        });
        next.add(newTag);
        return next;
      });

      setSelectedCategory('');
      setSelectedSubcategory('');
    }
  };

  const getValueDisplay = (value: string | SubValue): string => {
    if (typeof value === 'string') return value;
    if (value.name) {
      const extras = [];
      if (value.manufacturer) extras.push(`by ${value.manufacturer}`);
      if (value.capacities?.length) extras.push(`(${value.capacities.join(', ')})`);
      return `${value.name} ${extras.length ? extras.join(' ') : ''}`.trim();
    }
    return 'No description';
  };

  const handleValueSelect = (value: string) => {
    let newTag: string;
    
    if (currentCategory?.type === 'simple') {
      const valueData = currentCategory.values?.[value];
      newTag = formatTag(selectedCategory, null, value, valueData);
    } else if (currentCategory?.type === 'nested' && selectedSubcategory) {
      const valueData = currentCategory.subcategories?.[selectedSubcategory].values[value];
      newTag = formatTag(selectedCategory, selectedSubcategory, value, valueData);
    } else {
      return;
    }

    // Remove existing tag of the same category and add the new one
    setSelectedTags(prev => {
      const next = new Set(prev);
      Array.from(next).forEach(existingTag => {
        if (existingTag.startsWith(`#${selectedCategory}`)) {
          next.delete(existingTag);
        }
      });
      next.add(newTag);
      return next;
    });

    setSelectedCategory('');
    setSelectedSubcategory('');
  };

  const removeTag = (tag: string) => {
    setSelectedTags(prev => {
      const next = new Set(prev);
      next.delete(tag);
      return next;
    });
  };

  const copyToClipboard = () => {
    const text = Array.from(selectedTags).sort().join(' ');
    navigator.clipboard.writeText(text);
    alert('Tags copied to clipboard!');
  };

  const mainCategories = Object.entries(tagsData)
    .filter(([category]) => 
      // Filter only valid main categories
      category !== 'tag_structure' && 
      category !== 'search' &&
      (tagsData[category].type === 'simple' || tagsData[category].type === 'nested')
    )
    .map(([category, data]) => ({
      id: category,
      name: getCategoryDisplayName(category, data)
    }));

  function getCategoryDisplayName(category: string, data: TagData): string {
    // Use description if exists, otherwise format the category name
    return data.description || 
           category.split('_')
                  .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                  .join(' ');
  }

  const currentCategory = selectedCategory ? tagsData[selectedCategory] : null;

  // Add log to debug main categories
  console.log('Current tagsData:', tagsData);
  console.log('Main categories:', mainCategories);

  const hasValues = (category: TagData, subcategory?: string): boolean => {
    if (category.type === 'simple') {
      return Object.keys(category.values || {}).length > 0;
    } else if (category.type === 'nested' && subcategory) {
      return Object.keys(category.subcategories?.[subcategory].values || {}).length > 0;
    }
    return false;
  };

  const formatTagWithHighlight = (tag: string) => {
    // New regular expression that captures all components
    const matches = tag.match(/^([^#]*)([#])([^:>]*)(?:([:])?([^>]*))?(?:([>])(.*))?$/);
    
    if (!matches) return <span>{tag}</span>;
    
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const [_, name, hash, category, colon, subcategory, arrow, value] = matches;

    return (
      <span className="tag-highlight">
        <span className="tag-name">{name}</span>
        <span className="tag-separator">{hash}</span>
        <span className="tag-category">{category}</span>
        {colon && (
          <>
            <span className="tag-separator">{colon}</span>
            <span className="tag-subcategory">{subcategory}</span>
          </>
        )}
        {arrow && value && (
          <>
            <span className="tag-separator">{arrow}</span>
            <span className="tag-value">{value}</span>
          </>
        )}
      </span>
    );
  };

  return (
    <div className="app">
      <h1>Tag Generator</h1>

      <div className="category-section">
        <h3>Select Tags</h3>
        <div className="dropdown-group">
          <select value={selectedCategory} onChange={handleCategoryChange}>
            <option value="">Select Category...</option>
            {mainCategories.map(category => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </select>

          {currentCategory?.type === 'nested' && (
            <select value={selectedSubcategory} onChange={handleSubcategoryChange}>
              <option value="">Select Subcategory...</option>
              {Object.entries(currentCategory.subcategories || {}).map(([subcat, data]) => (
                <option key={subcat} value={subcat}>
                  {data.description || subcat.replace(/_/g, ' ')}
                </option>
              ))}
            </select>
          )}

          {((currentCategory?.type === 'simple' && hasValues(currentCategory)) ||
            (currentCategory?.type === 'nested' && selectedSubcategory && hasValues(currentCategory, selectedSubcategory))) && (
            <select 
              onChange={(e) => handleValueSelect(e.target.value)}
              value=""
              disabled={!selectedCategory || (currentCategory?.type === 'nested' && !selectedSubcategory)}
            >
              <option value="">Select Value...</option>
              {currentCategory?.type === 'simple' && currentCategory.values && 
                Object.entries(currentCategory.values)
                  .sort(([a], [b]) => a.localeCompare(b))
                  .map(([key, value]) => (
                    <option key={key} value={key}>
                      {getValueDisplay(value)}
                    </option>
                  ))
              }
              {currentCategory?.type === 'nested' && selectedSubcategory && 
                Object.entries(currentCategory.subcategories?.[selectedSubcategory].values || {})
                  .sort(([a], [b]) => a.localeCompare(b))
                  .map(([key, value]) => (
                    <option key={key} value={key}>
                      {getValueDisplay(value)}
                    </option>
                  ))
              }
            </select>
          )}
        </div>
      </div>

      <div className="selected-tags">
        <h3>Selected Tags:</h3>
        <div className="tags-list">
          {Array.from(selectedTags).sort().map(tag => (
            <span key={tag} className="tag">
              {formatTagWithHighlight(tag)}
              <button onClick={() => removeTag(tag)} title="Remove">&times;</button>
            </span>
          ))}
        </div>
      </div>

      <div className="output-section">
        <div className="highlighted-output">
          {Array.from(selectedTags).sort().map((tag, index) => (
            <React.Fragment key={tag}>
              {formatTagWithHighlight(tag)}
              {index < selectedTags.size - 1 && <span className="tag-separator"> </span>}
            </React.Fragment>
          ))}
        </div>
        <textarea
          readOnly
          value={Array.from(selectedTags).sort().join(' ')}
          placeholder="Selected tags will appear here..."
          style={{ opacity: 0, height: 0, position: 'absolute' }}
        />
        <button className="copy-btn" onClick={copyToClipboard}>
          Copy Tags
        </button>
      </div>
    </div>
  );
}

export default App;
