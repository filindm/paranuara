import unittest

from paranuara.app import app
from paranuara.models import Person
from ..base import TestBase


class TestPeopleFoodApi(TestBase):
    """
    Test get_persons_fav_food endpoint.
    """
    person_idx = 1
    base_url = '/people'
    favourite_food_url = f'{base_url}/{person_idx}/food'

    def test_favourite_food(self):
        name = 'Person One'
        age = 30
        fruits = sorted(["banana", "apple"])
        vegetables = sorted(["beetroot", "lettuce"])
        person = Person(
            index=self.person_idx,
            name=name,
            age=age,
            favourite_food=fruits + vegetables,
        ).save()
        with app.test_client() as client:
            r = client.get(self.favourite_food_url)
            self.assertEqual(r.status_code, 200)
            expected = {
                "username": name,
                "age": age,
                "fruits": fruits,
                "vegetables": vegetables,
            }
            actual = r.get_json()
            self.assertEqual(actual, expected)

    def test_favourite_food_no_such_person(self):
        with app.test_client() as client:
            r = client.get(self.favourite_food_url)
            self.assertEqual(r.status_code, 404)

