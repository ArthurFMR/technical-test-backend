from marshmallow import Schema


class BaseSchema(Schema):
    class Meta:
        strict = True  # To raise ValidationError
