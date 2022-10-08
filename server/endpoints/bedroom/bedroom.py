import datetime
import uuid

from flask import Blueprint, request
from security import jwt_required
from security.jwt_required import token_required
from helper.response.rest_response import Response
from database import changes
from service.bedroom.bedroom_service import BedroomService

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
        return BedroomService(app).get_data()
    if request.method == "POST":
        return BedroomService(app).set_data(current_user, request)
