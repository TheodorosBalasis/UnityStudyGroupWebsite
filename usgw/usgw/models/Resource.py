import json
from flask import jsonify
from usgw.util import success_json
from usgw.db import get_db
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
from ModelUtilities import to_json_response

db = get_db()


class Resource(object):
    required_fields = ['user_id', 'title', 'hyperlink', 'tags']
    fields = required_fields + ['uuid']

    def __init__(self, user_id, title, hyperlink, tags, uuid=None):
        # The UUID should be the id provided by MongoDB in the _id field.
        self.user_id = user_id
        self.title = title
        self.hyperlink = hyperlink
        self.tags = tags
        self.uuid = uuid

    @staticmethod
    def from_json(json):
        dict = json.loads(json)
        return Resource.from_dict(dict)

    @staticmethod
    def from_dict(dict):
        for key in dict:
            if key not in Resource.fields:
                raise ValueError('Invalid field ' + str(key))
        resource = Resource(dict['user_id'],
                            dict['title'],
                            dict['hyperlink'],
                            dict['tags'],
                            str(dict['_id']))
        return resource


def get_resource(id):
    resource = get_resource_by_id(id)
    return to_json_response(resource)


def post_resource(request):
    json_payload = json.dumps(request.get_json())
    payload_dict = json.loads(str(json_payload))
    for key in payload_dict:
        if key not in Resource.required_fields:
            return success_json(False, 'POST body contains invalid field ' + str(key))
    if len(payload_dict) < len(Resource.required_fields):
        return success_json(False, 'POST body has too few fields: ' + str(len(payload_dict)))
    resources = get_resources()
    resources.insert_one(payload_dict)
    return success_json(True, 'Request successful.')


def delete_resource(id):
    resources = get_resources()
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No document with id ' + str(id) + ' found.')
    resources.delete_one({'_id': ObjectId(id)})
    return success_json(True, 'Request completed successfully.')


def put_resource(id, request):
    json_payload = json.dumps(request.get_json())
    payload_dict = json.loads(str(json_payload))
    for key in payload_dict:
        if key not in Resource.required_fields:
            return success_json(False, 'PUT body contains invalid field ' + str(key))
    if len(payload_dict) == 0:
        return success_json(False, 'PUT body is empty.')
    resources = get_resources()
    if resources.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No resource found with id ' + str(id))
    document = resources.update_one({'_id': ObjectId(id)}, {'$set': payload_dict})
    return success_json(True, 'Request successful.')


def get_resource_by_id(id):
    resources = db['resources']
    if resources.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No resource found with id ' + str(id))
    resource = resources.find_one({"_id": ObjectId(id)})
    resource = Resource.from_dict(resource)
    return resource
