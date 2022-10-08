import datetime
import uuid

from flask import Blueprint, request
from security import jwt_required
from security.jwt_required import token_required
from helper.response.rest_response import Response
from database import changes

BEDROOM = Blueprint('bedroom', __name__)
app = None


def register_bedroom(apps):
    apps.register_blueprint(BEDROOM)
    global app
    app = apps
    jwt_required.set_app(app)


@BEDROOM.route('/bedroom', methods=["GET", "POST"])
@token_required
def bedroom(current_user):
    if request.method == "GET":
        a = 0
        _id = None
        while a == 0:
            change = changes.get_data_changes()
            if change:
                change = [dict(row) for row in change]
                changee = change[0]
                a = changee['is_valid']
                _id = changee['id']
        changes.set_executed_flag(_id)
        return Response.ok(changee['data'])
    if request.method == "POST":
        order = request.json
        post = order['data']
        request_id = changes.register_request(current_user, post)
        return Response.ok({"id": request_id})
