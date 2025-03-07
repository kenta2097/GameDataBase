from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

# Registrar rutas explícitamente
@freezer.register_generator
def index():
    yield {}  # Ruta raíz '/'

@freezer.register_generator
def generate():
    yield {}  # Ruta '/generate'

if __name__ == '__main__':
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_DESTINATION'] = 'build'
    freezer.freeze()
