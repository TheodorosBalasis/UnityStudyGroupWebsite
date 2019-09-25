from sys import stderr
from json import dumps
from flask import jsonify
from flask import Response


def atoi(obj: object) -> int:
    '''Convert object s to int without exception.'''
    try:
        return int(obj)
    except:
        return 0


def atob(obj: object) -> bool:
    '''Convert object s to bool without exception.'''
    return bool(atoi(obj))


def error_print(message: str) -> None:
    '''Print to the standard error output.'''
    stderr.write('\n%s\n\n' % (message,))


def json_response(successful: bool, message: str) -> Response:
    '''Generate a JSON response with a success and message fields.'''
    json_string = dumps({'success': successful, 'message': message})
    return jsonify(json_string)
