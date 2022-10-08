import datetime
import uuid

from database.database_connection import get_db_connection


def get_data_changes():
    conn = get_db_connection()
    change = conn.execute(
        "SELECT * FROM changes where is_valid = '1' ORDER BY created_on ASC LIMIT 1").fetchall()
    conn.close()
    return change


def set_executed_flag(_id):
    conn = get_db_connection()
    conn.execute(f"UPDATE changes SET is_valid = '0'  WHERE id ='{_id}'")
    conn.commit()
    conn.close()


def register_request(user, data):
    conn = get_db_connection()
    _id = uuid.uuid4().hex
    conn.execute(
        f"INSERT INTO changes (id, user_name, data, is_valid, created_on) values ('{_id}','{user}','{data}','1','{datetime.datetime.now().timestamp()}')")
    conn.commit()
    conn.close()
    return _id
