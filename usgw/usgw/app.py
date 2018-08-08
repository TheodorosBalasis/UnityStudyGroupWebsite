import os, json
from datetime import datetime
import mysql.connector as mysql
import flask
from flask import render_template as render
from usgw.config import Config

config = Config()
app    = flask.Flask(__name__)
app.secret_key = config['SECRET']

@app.route('/')
def index():
    return render('base.html', content="Hello World!")

