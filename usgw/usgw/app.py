from flask import render_template as render
from flask import request
import flask
import os

from pymongo.collection import Collection

from usgw.config import Config
from usgw.db import get_db
from usgw.models.Resource import Resource

config = Config()
app = flask.Flask(__name__)
app.secret_key = config['SECRET']


@app.route('/')
def index():
    db = get_db()
    return render('landing.html')


@app.route('/resources', methods=['GET', 'POST'])
def resources():
    if request.method is 'GET':
        return render('resources.html')
    elif request.method is 'POST':
        # Authentication stuff here
        post_resource(request.form)


@app.route('/contact')
def contact():
    return render('contact.html')


@app.route('/projects')
def projects():
    return render('projects.html')


@app.route('/resources/<uuid:id>', methods=['GET', 'DELETE'])
def get_resource_by_id(id):
    # type: (str) -> Resource
    if request.method is 'GET':
        return get_resource(id)
    elif request.method is 'DELETE':
        # Authentication stuff here
        delete_resource(id)


def get_resource(id):
    # type: (str) -> Resource
    resources_collection = get_resources()
    resource = resources_collection.find_one({"_id": id})
    resource = Resource.from_json(resource)
    return resource


def post_resource(request_form):
    # type: (dict) -> None
    pass


def delete_resource(id):
    # type: (str) -> None
    resources = get_resources()
    resources.delete_one({'_id': id})


def get_resources():
    # type: () -> Collection
    return db['resources']
