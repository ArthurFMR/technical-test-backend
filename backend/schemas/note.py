from marshmallow import fields
from .user import UserSchema
from .base_schema import BaseSchema


class NoteSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_date = fields.DateTime(dumb_only=True)
    user = fields.Nested(UserSchema, load_only=True)
