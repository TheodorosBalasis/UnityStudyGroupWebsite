from flask import render_template as render
from usgw.config import Config
import flask, os

config = Config()
app    = flask.Flask(__name__)
app.secret_key = config['SECRET']

@app.route('/')
def index():
    return render('base.html', content="Hello World!")

