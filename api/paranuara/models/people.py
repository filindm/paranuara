'''
Define Person model and serialisation schema.
'''
from marshmallow import Schema, fields

from ..db import db
from .mixins import Serializable


FRUITS = set(["strawberry", "apple", "banana", "orange"])
VEGGIES = set(["carrot", "beetroot", "celery", "cucumber", "lettuce"])


class PersonSchema(Schema):
    id = fields.String()
    index = fields.Integer()
    name = fields.String()
    username = fields.Function(lambda obj: obj.name)
    age = fields.Integer()
    address = fields.String()
    phone = fields.String()
    company_id = fields.Integer()
    fruits = fields.Method("get_favourite_fruits")
    vegetables = fields.Method("get_favourite_vegetables")

    def get_favourite_fruits(self, obj):
        return sorted(list(set(obj.favourite_food) & FRUITS))

    def get_favourite_vegetables(self, obj):
        return sorted(list(set(obj.favourite_food) & VEGGIES))


class Person(db.Document, Serializable):
    FRUITS = FRUITS
    VEGGIES = VEGGIES

    meta = {
        'collection': 'people',
    }
    _schema = {
        '': PersonSchema(only=('id', 'index', 'name', 'age', 'address', 'phone', 'company_id')),
        'fav_food': PersonSchema(only=('username', 'age', 'fruits', 'vegetables')),
        'info': PersonSchema(only=("name", "age", "address", "phone"))
    }

    index = db.IntField()
    name = db.StringField()
    age = db.IntField()
    address = db.StringField()
    phone = db.StringField()
    company_id = db.IntField()
    favourite_food = db.ListField(db.StringField(), db_field='favouriteFood')
    friends = db.ListField(db.DictField())
    eye_color = db.StringField(db_field='eyeColor')
    has_died = db.BooleanField()

    def get_friends_indexes(self):
        return [x['index'] for x in self.friends]

