import psycopg2
import os
from django.conf import settings

__all__ = ["connect", "exec_commands", "read_csv"]

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

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def convert_str_int_float(s):
    if is_float(s):
        if '.' in s:
            return float(s)
        else:
            return int(s)
    else:
        return s

def read_csv(filename) -> dict:
    filename = os.path.join(settings.BASE_DIR, "ex08", filename)
    f = open(filename)
    data = []
    if not os.path.isfile(filename):
        return data
    with open(filename, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip("\n")
            d = line.split('\t')
            values = list(map(convert_str_int_float, d))
            values.insert(0, i)
            data.append(values)
        f.close()
    return data
    