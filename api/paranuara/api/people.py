from flask import jsonify

from ..app import app
from ..models import Company, Person


@app.route('/people/<person_idx>/food', methods=['GET'])
def get_persons_fav_food(person_idx):
    """
    Given 1 person, provide a list of fruits and vegetables they like in the following format:
    {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
    """
    person = Person.objects.get_or_404(index=person_idx)
    return jsonify(Person.dump(person, schema='fav_food'))


@app.route('/people/<int:person1_idx>/<int:person2_idx>/friends', methods=['GET'])
def get_common_friends(person1_idx, person2_idx):
    """
    Given 2 people, provide their information (name, age, address, phone)
    and the list of their friends in common which have brown eyes and are still alive.
    """
    person1 = Person.objects.get_or_404(index=person1_idx)
    person2 = Person.objects.get_or_404(index=person2_idx)
    friends_indexes = sorted(list(set(person1.get_friends_indexes()) & set(person2.get_friends_indexes())))
    friends = Person.objects(index__in=friends_indexes, eye_color='brown', has_died=False)
    return jsonify({
        'person1': Person.dump(person1, schema='info'),
        'person2': Person.dump(person2, schema='info'),
        'friends': [f.index for f in friends],
    })
