#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import logging
from flask import Flask, request
from logging import Formatter, FileHandler
from models import db
from models.Notes import Note

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False
db.init_app(app)
db.app = app

with app.app_context():
    db.create_all()

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

#----------------------------------------------------------------------------#
# Routes.
#----------------------------------------------------------------------------#

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/health', methods=['GET'])
def api_health():
    return {
        "status": "OK"
    }

@app.route('/notes', methods=['GET', 'POST'])
def api_notes():
    if request.method == 'POST':
        data = request.get_json()
        n = Note(note=data['note'])
        db.session.add(n)
        db.session.commit()
        return {"status":"saved"}
    else:
        return Note.fs_get_delete_put_post()

@app.route('/note/<note_id>', methods=['GET', 'DELETE', 'PUT'])
def get_delete_put_note(note_id):
    return Note.fs_get_delete_put_post(note_id)

#----------------------------------------------------------------------------#
# Error handlers.
#----------------------------------------------------------------------------#

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "Oh No, 500 Server Error!", 500


@app.errorhandler(404)
def not_found_error(error):
    return "404, Nothing to see here!", 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
