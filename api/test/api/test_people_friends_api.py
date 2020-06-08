import unittest

from paranuara.app import app
from paranuara.models import Person
from ..base import TestBase


class TestPeopleFriendsApi(TestBase):
    """
    Test get_common_friends endpoint.
    """
    url = f'/people/0/1/friends'
    num_people = 5

    def setUp(self):
        super().setUp()
        self.people = [Person(
            index=n,
            name=f"name {n}",
            age=30 + n,
            address=f"address {n}",
            phone=f"phone {n}",
        ) for n in range(self.num_people)]

    def test_common_friends(self):

        # Friends in common: 2 and 3
        self.people[0].friends = [{'index': 1}, {'index': 2}, {'index': 3}, {'index': 4}]
        self.people[1].friends = [              {'index': 2}, {'index': 3}, {'index': 4}]

        # Friend 2 has wrong eye color - no match
        self.people[2].eye_color = 'red'
        self.people[2].has_died = False

        # Friend 3 has wrong eye color - match
        self.people[3].eye_color = 'brown'
        self.people[3].has_died = False

        # Friend 4 has died - no match
        self.people[4].eye_color = 'brown'
        self.people[4].has_died = True


        for person in self.people:
            person.save()
        self.assertEqual(Person.objects.count(), self.num_people)

        with app.test_client() as client:
            r = client.get(self.url)
            self.assertEqual(r.status_code, 200)
            expected = {
                "person1": {
                    "name": self.people[0].name,
                    "age": self.people[0].age,
                    "address": self.people[0].address,
                    "phone": self.people[0].phone,
                },
                "person2": {
                    "name": self.people[1].name,
                    "age": self.people[1].age,
                    "address": self.people[1].address,
                    "phone": self.people[1].phone,
                },
                "friends": [3],
            }
            actual = r.get_json()
            self.assertEqual(actual, expected)

    def test_common_friends_no_such_person(self):
        self.assertEqual(Person.objects.count(), 0)
        with app.test_client() as client:
            r = client.get(self.url)
            self.assertEqual(r.status_code, 404)

