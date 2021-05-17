from marshmallow import Schema, fields


class LoggerSchema(Schema):
    id = fields.Int(dump_only=True)
    token = fields.Str(required=True)