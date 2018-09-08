import json
import inspect
import types
from flask import jsonify


def to_json_response(model):
    '''Converts an object to a valid JSON response payload.'''
    return jsonify(json.dumps(model.__dict__))


def from_dict(dictionary, target_type):
    '''Converts a dictionary to an arbitrary heap type object.'''
    if not isinstance(dictionary, dict):
        raise TypeError('Dictionary argument is not a dictionary.')
    if not isinstance(target_type, (type, types.ClassType)):
        raise TypeError('Target type argument is not a type.')
    fields = get_fields(target_type)
    if not is_dict_instance(dictionary, target_type):
        raise ValueError('Dictionary argument contains keys that do not map to the target type\'s fields')
    new_object = type('temp', (object,), {})()
    new_object.__class__ = target_type
    type_methods = get_methods(target_type)
    for key in dictionary:
        setattr(new_object, key, dictionary[key])
    for method in type_methods:
        setattr(new_object, method[0], method[1])
    return new_object


def from_json(json_input, target_type):
    '''Converts a JSON input string to an object of an arbitrary heap type.'''
    if not isinstance(json_input, (str, unicode)):
        raise TypeError('JSON argument is not a string or unicode string.')
    dictionary = None
    try:
        dictionary = json.loads(json_input)
    except ValueError:
        raise ValueError('JSON input argument is an invalid JSON string.')
    return from_dict(dictionary, target_type)


def is_dict_instance(dictionary, target_type):
    '''Checks if the input dictionary is a serialized instance or partial instance of the target type.'''
    if not isinstance(dictionary, (dict,)):
        raise TypeError('Dictionary argument is not a dictionary.')
    if not isinstance(target_type, (type, types.ClassType)):
        raise TypeError('Target type argument is not a type.')
    fields = get_fields(target_type)
    for key in dictionary:
        if key not in fields:
            return False
    return True


def is_dict_instance_strict(dictionary, target_type):
    '''Checks if the input dictionary is a serialized instance of the target type, containing all its fields.'''
    if len(dictionary) == len(get_fields(target_type)):
        return is_dict_instance(dictionary, target_type)
    else:
        return False


def get_invalid_field(dictionary, target_type):
    '''Returns the first key that is an invalid field for the target type.'''
    if not isinstance(dictionary, (dict,)):
        raise TypeError('Dictionary argument is not a dictionary.')
    if not isinstance(target_type, (type, types.ClassType)):
        raise TypeError('Target type argument is not a type.')
    if is_dict_instance(dictionary, target_type):
        raise ValueError('Dictionary contains no invalid fields')
    fields = get_fields(target_type)
    for key in dictionary:
        if key not in fields:
            return key


def get_fields(target_type):
    '''Returns the instance fields of the target type based on its constructor.'''
    fields = None
    try:
        fields = inspect.getargspec(target_type.__init__).args
    except TypeError:
        raise TypeError('Type ' + target_type.__name__ + ' is not a heap type or has no constructor.')
    except AttributeError:
        raise AttributeError('Type ' + target_type.__name__ + ' has no constructor.')
    return fields[1:len(fields)]


def get_methods(target_type):
    '''Returns the instance methods of the target type, including dunder methods.'''
    if not isinstance(target_type, (type, types.ClassType)):
        raise TypeError('Target type is not a type.')
    return inspect.getmembers(target_type, predicate=inspect.ismethod)


def filter_dunder(method_list):
    if not isinstance(method_list, (list,)):
        raise TypeError('Method list is not a list.')
    return filter((lambda x: x[0][0:2] != '__'), method_list)
