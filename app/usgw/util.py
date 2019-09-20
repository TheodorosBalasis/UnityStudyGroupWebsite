import sys
import json
from flask import jsonify


def trim(s):
    try:
        return ' '.join(s.split())
    except:
        return s


def atoi(s):
    '''Convert object s to int without exception.'''
    try:
        return int(s)
    except:
        return 0


def atob(s):
    '''Convert object s to bool without exception.'''
    return bool(atoi(s))


def eprint(m):
    '''Print to the standard error output.'''
    try:
        m = str(m)
    except:
        m = 'ERR: bad conversion'
    sys.stderr.write('\n%s\n\n' % (m,))


def success_json(boolean, message):
    json_string = json.dumps({'success': boolean, 'message': message})
    return jsonify(json_string)
