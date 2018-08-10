from flask import render_template as render
from usgw.config import Config
import flask, os

config = Config()
app    = flask.Flask(__name__)
app.secret_key = config['SECRET']

@app.route('/')
def index():
    return ''

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