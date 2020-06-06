import unittest
from .base import TestBase
from paranuara.models import Company, Person


class TestDatabase(TestBase):

    def test_database_clean(self):
        self.assertEqual(Company.objects.count(), 0)
        self.assertEqual(Person.objects.count(), 0)
