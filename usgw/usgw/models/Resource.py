import json
from collections import namedtuple


class Resource:
    def __init__(self, uuid, user_id, title, hyperlink) -> str:
        # type: (str, str, str, str) -> None
        self.uuid = uuid
        self.user_id = user_id
        self.title = title
        self.hyperlink = hyperlink

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
                            named_tuple.hyperlink)
        return resource
