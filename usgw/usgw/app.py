import requests
import flask
from flask import render_template as render
from flask import request, redirect

from usgw.config import Config
from usgw.util import success_json
from usgw.models.resource import get_resource, post_resource, delete_resource, put_resource
from usgw.models.project import get_project, post_project, delete_project, put_project

config = Config()
app = flask.Flask(__name__)
app.secret_key = config['SECRET']


@app.route('/')
def index():
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


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        return render('projects.html')
    elif request.method == 'POST':
        # Authentication stuff here
        return post_project(request)
    else:
        return success_json(False, 'Invalid HTTP request method.')


@app.route('/projects/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def project(id):
    if request.method == 'GET':
        return get_project(id)
    elif request.method == 'DELETE':
        return delete_project(id)
    elif request.method == 'PUT':
        return put_project(id, request)
    else:
        return success_json(False, 'Invalid HTTP request method.')


@app.route('/slack/auth', methods=['GET'])
def log_in():
    code = request.args.get('code')
    origin_url = request.args.get('state')
    get_params = {'client_id': config['CLIENT_ID'],
                  'client_secret': config['CLIENT_SECRET'],
                  'code': code,
                  'redirect_uri': request.host + '/tokenreception'}
    requests.get('https://slack.com/api/oauth.access', get_params)
    return redirect(origin_url)


@app.route('/tokenreception', methods=['POST'])
def receive_token():
    response = request.get_json()


@app.route('/authredirecturl', methods=['GET'])
def get_auth_redirect_url():
    targetURL = 'https://slack.com/oauth/authorize'
    targetURL += '?'
    targetURL += 'client_id=' + config['CLIENT_ID']
    targetURL += '&' + 'scope=' + 'identity.basic'
    targetURL += '&' + 'team=' + config['TEAM_ID']
    return targetURL
