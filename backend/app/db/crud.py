# Imports
from .init_db import get_conn

# Function user created
def create_user_db(name: str, password: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users(name, password) VALUES(?,?)", (name, password))
    conn.commit()
    conn.close()

    return cursor.lastrowid

# Function get users
def get_users_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    return [dict(user) for user in users]

# Function get users
def get_users_name_db(name: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()

    if user is None:
        return None

    return dict(user)

# Function update user
def update_user_db(id: int, name: str, password: int):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name = ?, password = ?  WHERE id = ? ", (name, password, id))
    conn.commit()
    conn.close()

    return cursor.rowcount

# Fuction delete user
def delete_user_db(id: int):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return cursor.rowcount