from flask import request, jsonify
from helper.response.rest_response import Response
from flask import Blueprint
from endpoints.jwt_required import token_required, set_app

PING = Blueprint('ping', __name__)
app = None


def register_ping(apps):
    apps.register_blueprint(PING)
    global app
    app = apps


@PING.route('/ping', methods=['POST', 'GET', 'PUT'])
def ping():
    if request.method == 'GET':
        content = dict()
        content['method'] = request.method
        return jsonify(Response.ok(data=content))
    if request.method == 'POST':
        content = request.json
        content['method'] = request.method
        return jsonify(Response.ok(data=content))
    if request.method == 'PUT':
        content = request.json
        content['method'] = request.method
        return jsonify(Response.ok(data=content))
