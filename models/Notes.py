#----------------------------------------------------------------------------#
# Notes Model.
#----------------------------------------------------------------------------#
from . import db
from flask_serialize import FlaskSerializeMixin

FlaskSerializeMixin.db = db

class Note(db.Model, FlaskSerializeMixin):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(120), unique=False)

    # serializer fields
    create_fields = update_fields = ['note']

    def __init__(self, note=None):
        self.note = note

    def __repr__(self):
        return f'<Note {self.note!r}>'
