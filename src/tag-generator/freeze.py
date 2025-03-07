from flask_frozen import Freezer
from app import app
import os

freezer = Freezer(app)

# Registrar rutas explícitamente
@freezer.register_generator
def index():
    yield {}  # Ruta raíz '/'

@freezer.register_generator
def generate():
    yield {}  # Ruta '/generate'

@freezer.register_generator
def static():
    # Generar URLs para archivos estáticos
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), static_dir)
            yield {'filename': rel_path}

if __name__ == '__main__':
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_DESTINATION'] = 'build'
    app.config['FREEZER_STATIC_IGNORE'] = []  # No ignorar ningún archivo estático
    freezer.freeze()
