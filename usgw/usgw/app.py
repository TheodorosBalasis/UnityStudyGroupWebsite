from flask import render_template as render
from usgw.config import Config
from usgw.db import get_db
import flask, os

config = Config()
app    = flask.Flask(__name__)
app.secret_key = config['SECRET']

@app.route('/')
def index():
    db = get_db()
    return 'If this loads then you succesfully got the database!'

@app.route('/Resources')
def resources():
    return ''

@app.route('/Projects')
def projects():
    return ''

@app.route('/UnityAPI')
def unityAPI():
    return ''

@app.route('/Resources/<uuid:resourceID>')
def resource(resourceID):
    return ''

@app.route('/Projects/<uuid:projectID>')
def project(projectID):
    return ''
