import os
from marshmallow import Schema, fields, EXCLUDE
from dotenv_vault import load_dotenv
from lib import fields_custom as cfields


class EnvSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    API_URL = fields.Str(required=True)
    BOT_TOKEN = fields.Str(required=True)
    IP_TRUST_TIMEOUT_HOURS = cfields.IntStr(load_default=24)
    ABUSEIPDB_KEY = fields.Str()
    IP_ABUSE_CONFIDENCE_REJECTION_PERCENTAGE = cfields.IntStr(load_default=0)


load_dotenv()

env = EnvSchema().load(dict(os.environ))
