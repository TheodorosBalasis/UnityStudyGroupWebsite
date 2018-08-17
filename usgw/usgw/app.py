from flask import render_template as render
from flask import request, redirect, url_for
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


@app.route('/resources/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def resource(id):
    if request.method == 'GET':
        return get_resource(id)
    elif request.method == 'DELETE':
        return delete_resource(id)
    elif request.method == 'PUT':
        return put_resource(id, request)
    else:
        return success_json(False, 'Invalid HTTP request method.')


@app.route('/contact')
def contact():
    return render('contact.html')


@app.route('/projects')
def projects():
    db = get_db()

    data = []
    for doc in db.projects.find({}):
        data.append(doc)
        
    return render('projects.html', projects=data)

@app.route('/newproj')
def genproj():
    db = get_db()
    db.projects.insert_one({
        'author'      : 'Squirrelzar',
        'project'     : 'Crappy Game Name',
        'description' : 'This is the worst game you could ever imagine!',
        'link'        : 'www.google.com',
    })

    return redirect(url_for('projects'))
