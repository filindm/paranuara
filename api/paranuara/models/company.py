import marshmallow_mongoengine as ma
from ..db import db


class Company(db.Document):
    class Meta:
        schema = None

    index = db.IntField()
    name = db.StringField()

    def dump(self):
        self.Meta.schema.dump(self)


class CompanySchema(ma.ModelSchema):
    class Meta:
        model = Company


Company.Meta.schema = CompanySchema()

