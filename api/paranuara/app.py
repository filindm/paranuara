import os
from bson import json_util
from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGO_URI"]
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/companies')
def get_companies():
    items = mongo.db.companies.find()
    total = mongo.db.companies.count()
    return json_util.dumps({
        'items': list(items),
        'total': total,
    })
