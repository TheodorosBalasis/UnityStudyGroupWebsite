import json
from flask import jsonify
from usgw.util import success_json
from usgw.db import get_db
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId

db = get_db()


class Resource:
    requiredFields = ['user_id', 'title', 'hyperlink', 'tags']

    def __init__(self, user_id, title, hyperlink, tags, uuid=0):
        # type: (str, str, str, str, List[str]) -> None
        # The UUID should be the id provided by MongoDB in the _id field.
        self.uuid = uuid
        self.user_id = user_id
        self.title = title
        self.hyperlink = hyperlink
        self.tags = tags

    def to_json(self):
        # type: () -> str
        return json.dumps(self.__dict__)

    def to_json_response(self):
        return jsonify(self.to_json())

    @staticmethod
    def from_json(json):
        # type: (str) -> Resource
        dict = json.loads(json)
        return Resource.from_dict(dict)

    @staticmethod
    def from_dict(dict):
        # type: (dict) -> Resource
        resource = Resource(str(dict['_id']),
                            dict['user_id'],
                            dict['title'],
                            dict['hyperlink'],
                            dict['tags'])
        return resource


def get_resource(id):
    # type: (str) -> Resource
    resources_collection = get_resources()
    if resources_collection.find({"_id": ObjectId(id)}).count() == 0:
        return success_json(False, 'No resource found with id ' + str(id))
    resource = resources_collection.find_one({"_id": ObjectId(id)})
    resource = Resource.from_dict(resource)
    return resource.to_json_response()


def post_resource(request):
    # type: (dict) -> str
    json_payload = json.dumps(request.get_json())
    payload_dict = json.loads(str(json_payload))
    for key in payload_dict:
        if key not in Resource.requiredFields:
            return success_json(False, 'POST body contains invalid field ' + str(key))
    if len(payload_dict) < 4:
        return success_json(False, 'POST body has too few fields: ' + str(len(payload_dict)))
    resources = get_resources()
    resources.insert_one(payload_dict)
    return success_json(True, 'Request successful.')


def delete_resource(id):
    # type: (str) -> str
    resources = get_resources()
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No document with id ' + str(id) + ' found.')
    resources.delete_one({'_id': ObjectId(id)})
    return success_json(True, 'Request completed successfully.')


def put_resource(id, request_form):
    pass


def get_resources():
    # type: () -> Collection
    return db['resources']
