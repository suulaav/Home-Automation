from flask import Blueprint, jsonify, request
from flask_socketio import SocketIO, emit


from endpoints import jwt_required
from endpoints.jwt_required import token_required


BEDROOM = Blueprint('bedroom', __name__)
app = None


def register_bedroom(apps):
    apps.register_blueprint(BEDROOM)
    global app
    app = apps
    jwt_required.set_app(app)


@BEDROOM.route('/bedroom', methods=['POST'])
@token_required
def auth(user):
    data = request.json
    emit('response', {"user": user, "Light 1 is ": data["Light 1"], "Light 2 is ": data["Light 2"]}, broadcast=True,
         namespace='/')
    return {"user": user, "Light 1 is ": data["Light 1"], "Light 2 is ": data["Light 2"]}
