from flask import jsonify, request

from ..app import app
from ..models import Company, Person


@app.route('/companies/<int:company_id>/employees', methods=['GET'])
def get_company_employees(company_id):
    """
    Given a company, return all their employees.
    """
    Company.objects.get_or_404(index=company_id)
    default_page = 0
    default_page_size = 1000
    page = int(request.args.get('page', default_page))
    if page < 0:
        page = default_page
    per_page = int(request.args.get('per_page', default_page_size))
    if per_page <= 0:
        per_page = default_page_size
    employees = Person.objects(company_id=company_id)[page * per_page : (page + 1) * per_page]
    return jsonify({
        'employees': Person.dump(employees, many=True)
    })
