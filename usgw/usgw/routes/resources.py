from usgw.models.Resource import Resource
from usgw.db import get_db
from pymongo.collection import Collection

db = get_db()


def get_resources():
    # type: () -> Collection
    return db['resources']


def get_resource(id):
    # type: (str) -> Resource
    resources_collection = get_resources()
    resource = resources_collection.find_one({"uuid": id})
    resource = Resource.from_json(json)
    return resource


def post_resource():
    pass


def delete_resource():
    pass
