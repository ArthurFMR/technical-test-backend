from bottle import request, response

from marshmallow import ValidationError

from models.note import Note
from schemas.note import NoteSchema

from utils.manage_token import decode_token

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)  # Schema for Multiple objects


def create_note(token):
    user_data = decode_token(token)
    note_json = request.json

    # Validation of data
    try:
        note_data = note_schema.load(note_json).data
    except ValidationError as err:
        response.status = 422
        return {"error": err.messages}

     # Checking if note already exists
    try:
        Note.find_by_title(note_data['title'])
        message = "A note with that title already exists"
        response.status = 400
        return {"error": message}
    except:
        note = Note.create(user=user_data['identity'], **note_data)
        return {"note": note_schema.dump(note).data}


def get_notes(token):
    user_data = decode_token(token)

    notes = Note.find_all(user_data['identity'])
    return {"notes": notes_schema.dump(notes).data}
