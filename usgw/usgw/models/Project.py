import json
from flask import jsonify
from usgw.util import success_json
from usgw.db import get_db
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId

db = get_db()


class Project:
    required_fields = ['user_id', 'title', 'body']
    fields = required_fields + ['uuid']

    def __init__(self, user_id, title, body, uuid=0):
        # The UUID should be the id provided by MongoDB in the _id field.
        self.uuid = uuid
        self.user_id = user_id
        self.title = title
        self.body = body

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_json_response(self):
        return jsonify(self.to_json())

    @staticmethod
    def from_json(json):
        dict = json.loads(json)
        return project.from_dict(dict)

    @staticmethod
    def from_dict(dict):
        project = Project(dict['user_id'],
                          dict['title'],
                          dict['body'],
                          str(dict['_id']))
        return project


def get_project(id):
    project = get_project_by_id(id)
    return project.to_json_response()


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


def get_projects():
    return db['projects']


def get_project_by_id(id):
    projects = get_projects()
    if projects.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No project found with id ' + str(id))
    project = projects.find_one({"_id": ObjectId(id)})
    project = project.from_dict(project)
    return project
