import unittest

from paranuara.app import app
from paranuara.models import Company, Person
from ..base import TestBase


class TestCompanyEmployeesApi(TestBase):
    """
    Test get_company_employees endpoint.
    """
    company_id = 1
    url = f'/companies/{company_id}/employees'

    def test_employees(self):

        num_people = 30
        num_employees = 15
        per_page = 10

        Company(index=self.company_id, name="Company One").save()

        people = [Person(
            name=f'Person {n}',
            age=30 + n,
            address=f'address {n}',
            phone=f'phone {n}',
            company_id=self.company_id if n < num_employees else self.company_id + 1,
        ).save() for n in range(num_people)]

        self.assertEqual(Person.objects.count(), num_people)

        tests = [
            (0, people[:10]),
            (1, people[10:num_employees]),
            (2, []),
        ]
        for page, employees in tests:
            expected = {
                'employees': Person.dump(employees, many=True)
            }
            with app.test_client() as client:
                r = client.get(self.url, query_string=dict(page=page, per_page=per_page))
                self.assertEqual(r.status_code, 200)
                actual = r.get_json()
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

