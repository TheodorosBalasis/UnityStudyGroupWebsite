from flask import render_template as render
from flask import request
import flask
import os

from pymongo.collection import Collection

from usgw.config import Config
from usgw.db import get_db
from usgw.util import success_json
from usgw.models.Resource import Resource
from usgw.models.Resource import get_resource, post_resource, delete_resource, put_resource

config = Config()
app = flask.Flask(__name__)
app.secret_key = config['SECRET']


@app.route('/')
def index():
    db = get_db()
    return render('landing.html')


@app.route('/resources', methods=['GET', 'POST'])
def resources():
    if request.method == 'GET':
        return render('resources.html')
    elif request.method == 'POST':
        # Authentication stuff here
        return post_resource(request)
    else:
        return success_json(False, 'Invalid HTTP request method.')


@app.route('/resources/<uuid:id>', methods=['GET', 'DELETE', 'PUT'])
def resource(id):
    if request.method is 'GET':
        return get_resource(id)
    elif request.method is 'DELETE':
        return delete_resource(id)
    elif request.method is 'PUT':
        return put_resource(id, request.form)
    else:
        return success_json(False, 'Invalid HTTP request method.')


@app.route('/contact')
def contact():
    return render('contact.html')


@app.route('/projects')
def projects():
    return render('projects.html')
