from flask import jsonify

from ..app import app
from ..models import Company, Person


@app.route('/companies/<int:company_id>/employees', methods=['GET'])
def get_company_employees(company_id):
    """
    Given a company, return all their employees.
    """
    Company.objects.get_or_404(index=company_id)
    employees = Person.objects(company_id=company_id).all()
    return jsonify({
        'employees': Person.dump(employees, many=True)
    })
