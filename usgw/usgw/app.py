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
    return render(
        'base.html',
        content='If this loads then you succesfully got the database!'
    )
