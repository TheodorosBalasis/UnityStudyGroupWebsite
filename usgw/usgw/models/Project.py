from usgw.util import success_json
from usgw.db import get_db
from bson.objectid import ObjectId
from model_utilities import to_json_response, from_dict, from_json

db = get_db()


class Project(object):
    required_fields = ['user_id', 'title', 'body']
    fields = required_fields + ['_id']

    def __init__(self, user_id, title, body, _id=None):
        # The _id should be the id provided by MongoDB in the _id field.
        self.user_id = user_id
        self.title = title
        self.body = body
        self._id = _id


def get_project(id):
    project = get_project_by_id(id)
    return to_json_response(project)


def get_project_by_id(id):
    projects = db['projects']
    if projects.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No project found with id ' + str(id))
    project = projects.find_one({"_id": ObjectId(id)})
    project['_id'] = str(project['_id'])  # ObjectID type objects cannot be serialized to JSON.
    project = from_dict(project, Project)
    return project


def post_project(request):
    payload_dictionary = request.get_json()
    for key in payload_dictionary:
        if key not in Project.required_fields:
            return success_json(False, 'POST body contains invalid field ' + str(key))
    if len(payload_dictionary) < len(Project.required_fields):
        return success_json(False, 'POST body has too few fields: ' + str(len(payload_dictionary)))
    projects = db['projects']
    projects.insert_one(payload_dictionary)
    return success_json(True, 'Request successful.')


def delete_project(id):
    projects = db['projects']
    if projects.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No document with id ' + str(id) + ' found.')
    projects.delete_one({'_id': ObjectId(id)})
    return success_json(True, 'Request completed successfully.')


def put_project(id, request):
    payload_dictionary = request.get_json()
    for key in payload_dictionary:
        if key not in Project.required_fields:
            return success_json(False, 'PUT body contains invalid field ' + str(key))
    if len(payload_dictionary) == 0:
        return success_json(False, 'PUT body is empty.')
    projects = db['projects']
    if projects.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No project found with id ' + str(id))
    document = projects.update_one({'_id': ObjectId(id)}, {'$set': payload_dictionary})
    return success_json(True, 'Request successful.')
