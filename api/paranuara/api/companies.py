from flask import jsonify

from ..app import app
from ..models import Company, Person


@app.route('/companies/<int:company_id>/employees', methods=['GET'])
def get_company_employees(company_id):
    '''
    First check for existence of the company. Although not specified in the requirements,
    it might be a useful thing to do.
    If the company does exist, return all persons with the given company_id.
    '''
    Company.objects.get_or_404(index=company_id)
    employees = Person.objects(company_id=company_id).all()
    return jsonify({
        'employees': Person.dump(employees, many=True)
    })
