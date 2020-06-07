from flask import jsonify

from ..app import app
from ..models import Company, Person


@app.route('/people/<person_idx>/food', methods=['GET'])
def get_persons_fav_food(person_idx):
    person = Person.objects.get_or_404(index=person_idx)
    return jsonify(Person.dump(person, schema='fav_food'))
