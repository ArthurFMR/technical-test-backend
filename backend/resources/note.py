from bottle import HTTPResponse as http_res, request

from marshmallow import ValidationError

from models.note import Note
from schemas.note import NoteSchema

from utils.manage_token import decode_token

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


def create_note(token):
    user_data = decode_token(token)
    note_json = request.json

    # Validation of data
    try:
        note_data = note_schema.load(note_json).data
    except ValidationError as err:
        body = {"erros": err.messages}
        return http_res(status=422, body=body)
    
     # Checking if note already exists
    try:
        Note.find_by_title(note_data['title'])
        message = "A note with that title already exists"
        return http_res(status=400, body={"errors": message})
    except:
        note = Note.create(user=user_data['identity'], **note_data)
        body = {"note": note_schema.dump(note).data}
        return http_res(status=201, body=body)


def get_notes(token):
    user_data = decode_token(token)

    notes = Note.find_all(user_data['identity'])
    body = {"notes": notes_schema.dump(notes).data}
    return http_res(status=200, body=body)

