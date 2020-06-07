'''
Mixin class that adds serialization.
'''

class Serializable:

    _schema ={}

    @classmethod
    def dump(cls, obj, schema='', **kwargs):
        return cls._schema[schema].dump(obj, **kwargs)

