import psycopg2
__all__ = ["connect", "exec_commands"]

TABLE_NAME = "ex06_movies"

def connect():
    db = "djangotraining"
    username = "djangouser"
    password = "secret"
    conn = psycopg2.connect(f"dbname='{db}' user='{username}' host='127.0.0.1' password='{password}'")
    return conn

def exec_commands(cmds: list) -> None:
    conn = connect()
    cur = conn.cursor()
    for cmd in cmds:
        cur.execute(cmd)
    conn.commit()
    cur.close()
    conn.close()