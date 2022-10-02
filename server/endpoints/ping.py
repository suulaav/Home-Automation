import datetime
from flask import Flask, redirect, url_for, request
from response.rest_response import Response
from flask import Blueprint

PING = Blueprint('ping', __name__)


@PING.route('/ping', methods=['POST', 'GET', 'PUT'])
def ping():
    if request.method == 'POST':
        content = request.json
        content['method'] = request.method
        return Response.ok(data=content)
    if request.method == 'GET':
        return f"GET {datetime.datetime.now()}"
    if request.method == 'PUT':
        content = request.json
        content['method'] = request.method
        return Response.ok(data=content)
