import json
from flask import jsonify
from usgw.util import success_json
from usgw.db import get_db
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
from ModelUtilities import to_json_response
from ModelUtilities import from_dict

db = get_db()


class Project(object):
    required_fields = ['user_id', 'title', 'body']
    fields = required_fields + ['_id']

    def __init__(self, user_id, title, body, _id=None):
        # The UUID should be the id provided by MongoDB in the _id field.
        self.user_id = user_id
        self.title = title
        self.body = body
        self._id = _id

    @staticmethod
    def from_json(json):
        dict = json.loads(json)
        return project.from_dict(dict)


def get_project(id):
    project = get_project_by_id(id)
    return to_json_response(project)


def post_project(request):
    json_payload = json.dumps(request.get_json())
    payload_dict = json.loads(str(json_payload))
    for key in payload_dict:
        if key not in Project.required_fields:
            return success_json(False, 'POST body contains invalid field ' + str(key))
    if len(payload_dict) < len(Project.required_fields):
        return success_json(False, 'POST body has too few fields: ' + str(len(payload_dict)))
    projects = get_projects()
    projects.insert_one(payload_dict)
    return success_json(True, 'Request successful.')


def delete_project(id):
    projects = get_projects()
    if projects.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No document with id ' + str(id) + ' found.')
    projects.delete_one({'_id': ObjectId(id)})
    return success_json(True, 'Request completed successfully.')


def put_project(id, request):
    json_payload = json.dumps(request.get_json())
    payload_dict = json.loads(str(json_payload))
    for key in payload_dict:
        if key not in Project.required_fields:
            return success_json(False, 'PUT body contains invalid field ' + str(key))
    if len(payload_dict) == 0:
        return success_json(False, 'PUT body is empty.')
    projects = get_projects()
    if projects.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No project found with id ' + str(id))
    document = projects.update_one(
        {'_id': ObjectId(id)}, {'$set': payload_dict})
    return success_json(True, 'Request successful.')


def get_project_by_id(id):
    projects = db['projects']
    if projects.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No project found with id ' + str(id))
    project = projects.find_one({"_id": ObjectId(id)})
    project['_id'] = str(project['_id'])
    project = from_dict(project, Project)
    return project
