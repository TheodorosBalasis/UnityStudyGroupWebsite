import json
import inspect
from flask import jsonify


def to_json_response(model):
    return jsonify(json.dumps(model.__dict__))


def from_dict(dictionary, target_type):
    if type(dictionary) != dict:
        raise TypeError('Dictionary argument is not a dictionary.')
    if type(type) != type:
        raise TypeError('Target type argument is not a type.')
    fields = None
    try:
        fields = inspect.getargspec(target_type.__init__).args
    except AttributeError:
        raise AttributeError('Type ' + target_type.__name__ + ' has no constructor.')
    fields = fields[1:len(fields)]
    for key in dictionary:
        if key not in fields:
            raise ValueError('Invalid field ' + str(key))
        elif type(key) != str and type(key) != unicode:
            raise ValueError('Dictionary keys must be strings.')
    new_object = type('temp', (object,), {})()
    new_object.__class__ = target_type
    for key in dictionary:
        setattr(new_object, key, dictionary[key])
    type_methods = inspect.getmembers(type, predicate=inspect.ismethod)
    for method in type_methods:
        setattr(new_object, method[0], method[1])
    return new_object
