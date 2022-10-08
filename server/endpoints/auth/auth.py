import sqlite3

from flask import Blueprint, jsonify, make_response, request
from service.auths.auth_service import AuthenticateService
from helper.encode.base64_utils import encode
from database.user import get_user_credentials

AUTH = Blueprint('auth', __name__)
app = None


def register_auth(apps):
    apps.register_blueprint(AUTH)
    global app
    app = apps


@AUTH.route('/auths', methods=['POST'])
def auth():
    request_credentials = request.json
    if 'userName' not in request_credentials.keys() or 'password' not in request_credentials.keys():
        return make_response(jsonify({"message": "No userName or Password"}), 401)
    db_credentials = get_user_credentials(request_credentials)
    encoded_password = str(encode(request_credentials['password']))

    if db_credentials['user_name'] == request_credentials['userName'] and \
            db_credentials['password'] == encoded_password:
        return AuthenticateService(app).authenticate(request_credentials)
    else:
        return make_response(jsonify({"message": "Invalid userName or password"}), 401)
