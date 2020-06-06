import unittest
from mongoengine.connection import get_db


class TestBase(unittest.TestCase):

    def setUp(self):
        db = get_db()
        for col in db.list_collection_names():
            db.drop_collection(col)
