from functools import wraps
from flask import request, jsonify
import jwt

app = None


def set_app(apps):
    global app
    app = apps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        current_user = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['userName']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
