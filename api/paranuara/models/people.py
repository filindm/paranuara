from ..db import db


class Person(db.Document):
    meta = {
        'collection': 'people',
    }
    name = db.StringField()
    age = db.IntField()
    address = db.StringField()
    phone = db.StringField()
