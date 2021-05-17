from marshmallow import Schema, fields
from .user import UserSchema


class NotesSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_date = fields.DateTime(dumb_only=True)
    user = fields.Nested(UserSchema, load_only=True)