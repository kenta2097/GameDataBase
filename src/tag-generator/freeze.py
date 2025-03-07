from flask_frozen import Freezer
from app import app
import os

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield {}

@freezer.register_generator
def generate():
    yield {}

@freezer.register_generator
def static():
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            rel_dir = os.path.relpath(root, static_dir)
            if rel_dir == '.':
                yield {'filename': file}
            else:
                yield {'filename': os.path.join(rel_dir, file)}

if __name__ == '__main__':
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_DESTINATION'] = 'build'
    app.config['FREEZER_STATIC_IGNORE'] = []  # No ignorar ningún archivo estático
    app.config['FREEZER_BASE_URL'] = '/GameDataBase/tag-generator/'
    app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
    freezer.freeze()
