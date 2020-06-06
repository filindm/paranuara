from ..db import db


class Company(db.Document):
    meta = {
        'collection': 'companies',
    }
    index = db.IntField()
    name = db.StringField()
