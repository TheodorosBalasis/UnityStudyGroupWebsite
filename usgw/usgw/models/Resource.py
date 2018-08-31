from usgw.util import success_json
from usgw.db import get_db
from bson.objectid import ObjectId
from ModelUtilities import to_json_response, from_dict, from_json

db = get_db()


class Resource(object):
    required_fields = ['user_id', 'title', 'hyperlink', 'tags']
    fields = required_fields + ['_id']

    def __init__(self, user_id, title, hyperlink, tags, _id=None):
        # The _id should be the id provided by MongoDB in the _id field.
        self.user_id = user_id
        self.title = title
        self.hyperlink = hyperlink
        self.tags = tags
        self._id = _id


def get_resource(id):
    resource = get_resource_by_id(id)
    return to_json_response(resource)


def get_resource_by_id(id):
    resources = db['resources']
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No resource found with id ' + str(id))
    resource = resources.find_one({'_id': ObjectId(id)})
    resource['_id'] = str(resource['_id'])  # ObjectID type objects cannot be serialized to JSON.
    resource = from_dict(resource, Resource)
    return resource


def post_resource(request):
    payload_dictionary = request.get_json()
    for key in payload_dictionary:
        if key not in Resource.required_fields:
            return success_json(False, 'POST body contains invalid field ' + str(key))
    if len(payload_dictionary) < len(Resource.required_fields):
        return success_json(False, 'POST body has too few fields: ' + str(len(payload_dictionary)))
    resources = db['resources']
    resources.insert_one(payload_dictionary)
    return success_json(True, 'Request successful.')


def delete_resource(id):
    resources = db['resources']
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No document with id ' + str(id) + ' found.')
    resources.delete_one({'_id': ObjectId(id)})
    return success_json(True, 'Request completed successfully.')


def put_resource(id, request):
    payload_dictionary = request.get_json()
    for key in payload_dictionary:
        if key not in Resource.required_fields:
            return success_json(False, 'PUT body contains invalid field ' + str(key))
    if len(payload_dictionary) == 0:
        return success_json(False, 'PUT body is empty.')
    resources = db['resources']
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No resource found with id ' + str(id))
    document = resources.update_one({'_id': ObjectId(id)}, {'$set': payload_dictionary})
    return success_json(True, 'Request successful.')
