from django.db import models
from psycopg2.extras import RealDictCursor

from . import connect, exec_commands

# Create your models here.
class MovieModel:
    __TABLE_NAME__ = "ex06_movies"

    def __init__(self) -> None:
        self.conn = connect()
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def setup(sef):
        pass

    def get(self, where: dict):
        wherer = self.dict_to_setter(where)
        self.cur.execute(f"SELECT * FROM {self.__TABLE_NAME__} WHERE {wherer} limit 1")
        row = self.cur.fetchone()
        selected = dict(row) if row else None
        self.cur.close()
        return selected

    def list(self):
        self.cur.execute(f"SELECT * FROM {self.__TABLE_NAME__}")
        rows = self.cur.fetchall()
        self.cur.close()
        return [ dict(r) for r in rows]

    def bulk_insert(self, data: dict):
        fields = list(data[0].keys())
        cmds = []
        for d in data:
            cmd = f"INSERT INTO {self.__TABLE_NAME__} ({','.join(fields)}) VALUES {tuple(d.values())}"
            cmds.append(cmd)
        exec_commands(cmds)

    def update(self, where: dict, data: dict):
        setter = self.dict_to_setter(data)
        wherer = self.dict_to_setter(where)
        cmd = f"UPDATE {self.__TABLE_NAME__} SET {setter} WHERE {wherer}"
        self.cur.execute(cmd)
        self.conn.commit()
        self.cur.close()
    
    def remove(self, where: dict):
        wherer = self.dict_to_setter(where)
        cmd = f"DELETE FROM {self.__TABLE_NAME__} WHERE {wherer}"
        self.cur.execute(cmd)
        self.conn.commit()
        self.cur.close()

    def dict_to_setter(self, dt: dict) -> str:
        ss = ','.join([f"{key} = '{val}'" for key, val in dt.items()])
        return ss
