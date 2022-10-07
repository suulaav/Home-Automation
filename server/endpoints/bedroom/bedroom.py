import json
import sqlite3
import time
import datetime
import uuid

from flask import Blueprint, jsonify, request
from security import jwt_required
from security.jwt_required import token_required
from helper.response.rest_response import Response

BEDROOM = Blueprint('bedroom', __name__)
app = None


def register_bedroom(apps):
    apps.register_blueprint(BEDROOM)
    global app
    app = apps
    jwt_required.set_app(app)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@BEDROOM.route('/bedroom', methods=["GET", "POST"])
@token_required
def bedroom(current_user):
    conn = get_db_connection()
    if request.method == "GET":
        a = 0
        id = None
        while a == 0:
            change = conn.execute(
                "SELECT * FROM changes where is_valid = '1' ORDER BY created_on ASC LIMIT 1").fetchall()
            if change:
                change = [dict(row) for row in change]
                changee = change[0]
                a = changee['is_valid']
                id = changee['id']
        conn.execute(f"UPDATE changes SET is_valid = '0'  WHERE id ='{id}'")
        conn.commit()
        return Response.ok(changee['data'])
    if request.method == "POST":
        order = request.json
        post = order['data']
        conn.execute(
            f"INSERT INTO changes (id, user_name, data, is_valid, created_on) values ('{uuid.uuid4().hex}','{current_user}','{post}','1','{datetime.datetime.now().timestamp()}')")
        conn.commit()
        return "ok"
