import json
from collections import namedtuple


class Resource:
    def __init__(self, uuid, user_id, title, hyperlink, tags):
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

    def from_json(json):
        # type: (str) -> Resource
        dict = json.loads(json)
        named_tuple = namedtuple('Resource', dict.keys())(*dict.values())
        resource = Resource(named_tuple.uuid,
                            named_tuple.user_id,
                            named_tuple.title,
                            named_tuple.hyperlink,
                            named_tuple.tags)
        return resource


def get_resource(id):
    # type: (str) -> Resource
    resources_collection = get_resources()
    resource = resources_collection.find_one({"_id": id})
    resource = Resource.from_json(resource)
    return resource


def post_resource(request_form):
    # type: (dict) -> None
    pass


def delete_resource(id):
    # type: (str) -> None
    resources = get_resources()
    resources.delete_one({'_id': id})


def put_resource(id, request_form):
    pass


def get_resources():
    # type: () -> Collection
    return db['resources']
