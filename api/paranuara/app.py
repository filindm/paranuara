import os

from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from werkzeug.exceptions import HTTPException

from .db import db


app = Flask(__name__)
app.config["MONGODB_DB"] = os.environ["MONGODB_DB"]
app.config['MONGODB_HOST'] = os.environ["MONGODB_HOST"]
db.init_app(app)
from . import api


@app.route('/health')
def health():
    return jsonify(ok=True)


@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }), e.code
