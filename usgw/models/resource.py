from usgw.util import success_json
from usgw.db import get_db
from bson.objectid import ObjectId
from .model_utilities import to_json_response, from_dict, from_json
from .model_utilities import is_dict_instance, is_dict_instance_strict, get_invalid_field

db = get_db()


class Resource(object):
    def __init__(self, user_id, title, hyperlink, tags, _id=None):
        # The _id should be the id provided by MongoDB in the _id field.
        self.user_id = user_id
        self.title = title
        self.hyperlink = hyperlink
        self.tags = tags
        self._id = _id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


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
    payload = request.get_json()
    if not is_dict_instance_strict(payload, Resource):
        return success_json(False, 'POST body is invalid Resource instance.')
    resources = db['resources']
    resources.insert_one(payload)
    return success_json(True, 'Request successful.')


def delete_resource(id):
    resources = db['resources']
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No document with id ' + str(id) + ' found.')
    resources.delete_one({'_id': ObjectId(id)})
    return success_json(True, 'Request completed successfully.')


def put_resource(id, request):
    payload = request.get_json()
    if not is_dict_instance(payload, Project):
        return success_json(False, 'PUT body contains invalid field: {}'
                            .format(get_invalid_field(payload, Resource)))
    if len(payload) == 0:
        return success_json(False, 'PUT body is empty.')
    resources = db['resources']
    if resources.find({'_id': ObjectId(id)}).count() == 0:
        return success_json(False, 'No resource found with id ' + str(id))
    document = resources.update_one({'_id': ObjectId(id)}, {'$set': payload})
    return success_json(True, 'Request successful.')
