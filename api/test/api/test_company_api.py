import unittest

from paranuara.app import app
from paranuara.models import Company, Person
from ..base import TestBase


class TestCompanyApi(TestBase):

    company_id = 1
    url = f'/companies/{company_id}/employees'

    def test_employees(self):
        Company(index=self.company_id, name="Company One").save()
        expected = [
            Person(
                name='Person One',
                age=30,
                address='address one',
                phone='phone one',
                company_id=self.company_id,
            ).save(),
            Person(
                name='Person Two',
                age=30,
                address='address two',
                phone='phone two',
                company_id=self.company_id,
            ).save(),
        ]
        Person(
            name='Person Three',
            age=30,
            address='address three',
            phone='phone three',
            company_id=self.company_id + 1,
        ).save()
        expected = Person.dump(expected, many=True)
        with app.test_client() as client:
            r = client.get(self.url)
            self.assertEqual(r.status_code, 200)
            actual = r.get_json()['employees']
            self.assertEqual(actual, expected)

    def test_employees_no_company(self):
        with app.test_client() as client:
            r = client.get(self.url)
            self.assertEqual(r.status_code, 404)

    def test_employees_empty(self):
        Company(index=self.company_id, name="Company One").save()
        with app.test_client() as client:
            r = client.get(self.url)
            self.assertEqual(r.status_code, 200)
            expected = []
            actual = r.get_json()['employees']
            self.assertEqual(actual, expected)

