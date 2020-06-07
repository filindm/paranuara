'''
Define Person model and serialisation schema.
'''
from marshmallow import Schema, fields

from ..db import db
from .mixins import Serializable


class PersonSchema(Schema):
    id = fields.String()
    name = fields.String()
    age = fields.Integer()
    address = fields.String()
    phone = fields.String()
    company_id = fields.Integer()


class Person(db.Document, Serializable):
    meta = {
        'collection': 'people',
    }
    _schema = {
        '': PersonSchema(),
    }

    name = db.StringField()
    age = db.IntField()
    address = db.StringField()
    phone = db.StringField()
    company_id = db.IntField()

