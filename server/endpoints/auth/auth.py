import sqlite3

from flask import Blueprint, jsonify, make_response, request
from service.auths.auth_service import Authenticate
from helper.encode.base64_utils import encode

AUTH = Blueprint('auth', __name__)
app = None


def register_auth(apps):
    apps.register_blueprint(AUTH)
    global app
    app = apps


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@AUTH.route('/auths', methods=['POST'])
def auth():
    conn = get_db_connection()
    request_credentials = request.json
    if 'userName' not in request_credentials.keys() or 'password' not in request_credentials.keys():
        return make_response(jsonify({"message": "No userName or Password"}), 401)

    db_credentials = conn.execute(
        f"SELECT * FROM users where user_name = '{request_credentials['userName']}' ORDER BY created_on ASC LIMIT 1").fetchone()
    db_credentials = dict(db_credentials)
    encoded_password = str(encode(request_credentials['password']))

    if db_credentials['user_name'] == request_credentials['userName'] and db_credentials[
        'password'] == encoded_password:
        return Authenticate(app).authenticate(request_credentials)
    else:
        return make_response(jsonify({"message": "Invalid UserName or Password"}), 401)
