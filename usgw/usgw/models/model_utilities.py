import json
import inspect
from flask import jsonify


def to_json_response(model):
    '''Converts an object to a valid JSON response payload.'''
    return jsonify(json.dumps(model.__dict__))


def from_dict(dictionary, target_type):
    '''Converts a dictionary to an arbitrary heap type object.'''
    if type(dictionary) != dict:
        raise TypeError('Dictionary argument is not a dictionary.')
    if type(target_type) != type:
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


def from_json(json_input, target_type):
    '''Converts a JSON input string to an object of an arbitrary heap type.'''
    if type(json_input) != str and type(json_input) != unicode:
        raise TypeError('JSON argument needs to be a string.')
    if type(target_type) != type:
        raise TypeError('Target type argument is not a type.')
    dictionary = None
    try:
        dictionary = json.loads(json_input)
    except ValueError:
        raise ValueError('JSON input argument is an invalid JSON string.')
    return from_dict(dictionary, target_type)
