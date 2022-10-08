import datetime
import os
from service.auths.AuthInterface import AuthenticateInterface
from flask import jsonify
from helper.response.rest_response import Response
import jwt


class AuthenticateService(AuthenticateInterface):
    def __init__(self, app):
        self.app = app

    def authenticate(self, credential):
        user_name = credential['userName']
        password = credential['password']
        temp_username = os.getenv("username")
        temp_password = os.getenv("password")

        if not user_name == temp_username or not password == temp_password:
            return jsonify({"message": "Check Credentials"}), 401

        token = jwt.encode({"userName": user_name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           self.app.config['SECRET_KEY'])
        return jsonify(Response.ok({'token': token}))
