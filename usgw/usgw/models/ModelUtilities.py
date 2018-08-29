import json
from flask import jsonify

def to_json_response(model):
        return jsonify(json.dumps(model.__dict__))
