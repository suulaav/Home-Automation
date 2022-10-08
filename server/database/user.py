from database.database_connection import get_db_connection


def get_user_credentials(user):
    conn = get_db_connection()
    credentials = conn.execute(
        f"SELECT * FROM users where user_name = '{user['userName']}' ORDER BY created_on ASC LIMIT 1").fetchone()
    conn.close()
    return dict(credentials)
