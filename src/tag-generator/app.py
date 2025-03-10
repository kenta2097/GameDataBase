from flask import Flask, render_template, request, flash, jsonify, url_for, send_from_directory
import yaml
from jinja2 import StrictUndefined
import os

# Definir rutas de archivos y directorios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def get_config_file():
    # Buscar el archivo en la raíz primero
    root_config = os.path.join(BASE_DIR, 'tags.yml')
    if os.path.exists(root_config):
        return root_config
    
    # Si no está en la raíz, buscar en el directorio actual
    local_config = os.path.join(os.path.dirname(__file__), 'tags.yml')
    if os.path.exists(local_config):
        return local_config
    
    return root_config  # Devolver la ruta raíz por defecto

CONFIG_FILE = get_config_file()

app = Flask(__name__, 
           static_url_path='/static',  # Añadido slash inicial
           static_folder='static')
app.secret_key = 'gamedatabase_secret_key'

# Actualizar configuración
app.config.update(
    FREEZER_RELATIVE_URLS=False,  # Cambiado a False
    FREEZER_DESTINATION='build',
    FREEZER_BASE_URL='http://localhost:5000'  # URL base para generación
)

# Función helper corregida para URLs estáticas
def static_url(filename):
    if not filename:
        return ''
    return url_for('static', filename=filename)

# Hacer la función disponible en las plantillas
app.jinja_env.globals.update(static_url=static_url)

def is_valid_dict(obj):
    try:
        return isinstance(obj, dict) and bool(obj)
    except:
        return False

def safe_get_value(dict_obj, key, default=None):
    try:
        return dict_obj.get(str(key), default) if isinstance(dict_obj, dict) else default
    except:
        return default

def convert_keys_to_str(data):
    if isinstance(data, dict):
        return {str(k): convert_keys_to_str(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_str(item) for item in data]
    return data

def load_tags():
    try:
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError(f"No tags.yml found in {CONFIG_FILE}")
                
        with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            # Convert numeric keys to strings in the entire data structure
            data = convert_keys_to_str(data)
            if not is_valid_dict(data):
                raise ValueError("No valid data in tags file")
            print(f"Tags loaded successfully from {CONFIG_FILE}")
            return data
    except Exception as e:
        print(f"Error loading tags from {CONFIG_FILE}: {e}")
        return {}

# Load tags with error handling
tags_data = load_tags()

def generate_tag_string(category, subcategory=None, value=None):
    try:
        if subcategory and value:
            return f"#{str(category)}:{str(subcategory)}>{str(value)}"
        elif subcategory:
            return f"#{str(category)}:{str(subcategory)}"
        elif value:
            return f"#{str(category)}>{str(value)}"
        else:
            return f"#{str(category)}"
    except Exception as e:
        print(f"Error generating tag string: {e}")
        return ""

@app.route('/')
def index():
    if not tags_data:
        flash("Could not load tags data. Using empty configuration.", "warning")
        return render_template('index.html', 
                             tags={}, 
                             is_valid_dict=is_valid_dict,
                             safe_get_value=safe_get_value)
    
    return render_template('index.html', 
                         tags=tags_data, 
                         is_valid_dict=is_valid_dict,
                         safe_get_value=safe_get_value)

@app.route('/generate', methods=['POST'])
def generate():
    selected_tags = []
    try:
        form_data = request.form.to_dict()
        
        for key, value in form_data.items():
            if value and value.strip():  # Check if value is not empty
                parts = key.split('_')
                try:
                    if len(parts) == 3:  # category_subcategory_value
                        tag = generate_tag_string(parts[0], parts[1], parts[2])
                    elif len(parts) == 2:  # category_value
                        tag = generate_tag_string(parts[0], value=parts[1])
                    else:
                        tag = generate_tag_string(parts[0], value)
                    
                    if tag:  # Only add if a valid tag was generated
                        selected_tags.append(tag)
                except Exception as e:
                    print(f"Error processing tag {key}: {e}")
                    continue
                    
    except Exception as e:
        print(f"Error processing form: {e}")
        flash("Error processing selected tags", "error")
    
    return render_template('result.html', 
                         selected_tags=selected_tags,
                         has_tags=bool(selected_tags))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
