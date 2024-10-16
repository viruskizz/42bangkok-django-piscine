from django.db import models
from psycopg2.extras import RealDictCursor

from . import connect, exec_commands

# Create your models here.
class MovieModel:
    __TABLE_NAME__ = "ex06_movies"

    def __init__(self) -> None:
        self.conn = connect()
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def setup(self):
        create_table_cmd = f"""
            CREATE TABLE IF NOT EXISTS {self.__TABLE_NAME__} (
                title VARCHAR(64) NOT NULL UNIQUE,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP NOT NULL,
                updated TIMESTAMP NOT NULL
            )
        """
        create_func_created_cmd = f"""
            CREATE OR REPLACE FUNCTION create_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.created = now();
                NEW.updated = now();
                RETURN NEW;
            END
            $$ language 'plpgsql';
            CREATE TRIGGER create_changetimestamp_column BEFORE INSERT
            ON {self.__TABLE_NAME__} FOR EACH ROW EXECUTE PROCEDURE
            create_changetimestamp_column();
        """
        create_func_updated_cmd = f"""
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON {self.__TABLE_NAME__} FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
        """
        exec_commands([create_table_cmd, create_func_created_cmd, create_func_updated_cmd])

    def get(self, where: dict):
        wherer = self.dict_to_setter(where)
        self.cur.execute(f"SELECT * FROM {self.__TABLE_NAME__} WHERE {wherer} limit 1")
        row = self.cur.fetchone()
        selected = dict(row) if row else None
        self.cur.close()
        return selected

    def list(self):
        try:
            self.cur.execute(f"SELECT * FROM {self.__TABLE_NAME__}")
            rows = self.cur.fetchall()
            self.cur.close()
            return [ dict(r) for r in rows]
        except Exception as e:
            print(e)
            return []

    def bulk_insert(self, data: list):
        fields = list(data[0].keys())
        results = []
        for d in data:
            cmd = f"INSERT INTO {self.__TABLE_NAME__} ({','.join(fields)}) VALUES {tuple(d.values())}"
            try:
                self.cur.execute(cmd)
                results.append({'title': d['title'], 'status': True, 'message': 'OK'})
            except Exception as e:
                results.append({'title': d['title'], 'status': False, 'message': str(e)})
            self.conn.commit()
        return results

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
