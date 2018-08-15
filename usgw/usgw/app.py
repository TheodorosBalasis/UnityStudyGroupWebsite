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
    return render('landing.html')

@app.route('/contact')
def contact():
    return render('contact.html')

@app.route('/projects')
def projects():
    return render('projects.html')

@app.route('/resources')
def resources():
    return render('resources.html')
