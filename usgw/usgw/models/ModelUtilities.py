import json
import inspect
from flask import jsonify

from usgw.models.Resource import Resource


def to_json_response(model):
    return jsonify(json.dumps(model.__dict__))


def from_dict(dictionary, target_type):
    if type(dictionary) != dict:
        raise TypeError('Dictionary argument is not a dictionary.')
    if type(type) != type:
        raise TypeError('Target type argument is not a type.')
    fields = None
    try:
        fields = inspect.getargspec(target_type.__init__)
    except AttributeError:
        raise AttributeError('Type ' + target_type.__name__ + ' has no constructor.')
    fields = fields[1:len(fields)]
    for key in dictionary:
        if key not in fields:
            raise ValueError('Invalid field ' + str(key))
    new_object = type('', (), dictionary)
    new_object.__class__ = target_type
    return new_object
