'''
Define Company model and serialisation schema.
'''
from marshmallow import Schema, fields

from ..db import db
from .mixins import Serializable


class CompanySchema(Schema):
    id = fields.String()
    index = fields.Integer()
    name = fields.String()


class Company(db.Document, Serializable):
    meta = {
        'collection': 'companies',
    }
    _schema = {
        '': CompanySchema(),
    }

    index = db.IntField()
    name = db.StringField()

