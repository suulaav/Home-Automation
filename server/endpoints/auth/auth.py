from flask import Blueprint, jsonify, make_response, request
from service.auths.auth_service import Authenticate

AUTH = Blueprint('auth', __name__)
app = None


def register_auth(apps):
    apps.register_blueprint(AUTH)
    global app
    app = apps


@AUTH.route('/auths', methods=['POST'])
def auth():
    credential = request.json
    if 'userName' not in credential.keys() or 'password' not in credential.keys():
        return make_response(jsonify({"message": "No userName or Password"}), 401)
    else:
        return Authenticate(app).authenticate(credential)
