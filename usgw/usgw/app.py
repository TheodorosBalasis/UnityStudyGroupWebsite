from flask import render_template as render
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


@app.route('/join')
def join():
    return render('join.html')


@app.route('/resources')
def resources():
    return render('resources.html')


@app.route('/projects')
def projects():
    return render('projects.html')


@app.route('/resources/<id>')
def get_resource_by_id(id):
    # type: (str) -> Resource
    resources_collection = get_resources()
    resource = resources_collection.find_one({"uuid": id})
    resource = Resource.from_json(json)
    return resource


def post_resource():
    pass


def delete_resource():
    pass


def get_resources():
    # type: () -> Collection
    return db['resources']
