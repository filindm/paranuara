import os
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from .db import db
from .models import (
    Company,
    Person,
)


app = Flask(__name__)
app.config["MONGODB_DB"] = os.environ["MONGODB_DB"]
app.config['MONGODB_HOST'] = os.environ["MONGODB_HOST"]
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/companies')
def get_companies():
    companies = Company.objects[:10]
    total = Company.objects.count()
    return jsonify({
        'companies': list(companies),
        'total': total,
    })
