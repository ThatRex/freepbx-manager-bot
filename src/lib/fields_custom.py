from marshmallow import fields, ValidationError


class IntStr(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if value.isdigit():
            return int(value)
        raise ValidationError("Field must contain only numerical characters.")
