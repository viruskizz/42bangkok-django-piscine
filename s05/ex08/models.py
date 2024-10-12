from typing import Any
from django.db import models
from . import connect, exec_commands
from psycopg2.extras import RealDictCursor

class DbBaseModel:
    __TABLE_NAME__ = None
    __FIELDS__ = None

    def __init__(self) -> None:
        self.conn = connect()
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def setup(self):
        pass

    def data_null_covert(data: list):
        d = []
        for values in data:
            values = [ None if v == 'NULL' else v for v in values ]
            d.append(values)
        return d

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

    def bulk_insert(self, data: list):
        value_args = ["%s" for x in range(len(self.__FIELDS__))]
        cmd = f"""
            INSERT INTO {self.__TABLE_NAME__} ({','.join(self.__FIELDS__)})
            VALUES ({",".join(value_args)})
        """
        for d in data:
            self.cur.execute(cmd, d)
        self.conn.commit()

    def bulk(self, data: list):
        cmd = f"INSERT INTO {self.__TABLE_NAME__} ({', '.join(self.__FIELDS__)}) VALUES "
        cmd += f"{','.join([str(tuple(v)) for v in data])}"
        exec_commands([cmd])

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
    
    def load_data(filename: str):
        pass

# Create your models here.
class PlanetModel(DbBaseModel):
    __TABLE_NAME__ = "ex08_planets"
    __FIELDS__ = ['id', 'name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']

    def setup(self):
        create_table_cmd = f"""
            CREATE TABLE IF NOT EXISTS {self.__TABLE_NAME__} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) NOT NULL UNIQUE,
                climate VARCHAR,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            )
        """
        exec_commands([create_table_cmd])

class PeopleModel(DbBaseModel):
    __TABLE_NAME__ = "ex08_people"
    __FIELDS__ = ['id', 'name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld']

    def setup(self):
        create_table_cmd = f"""
            CREATE TABLE IF NOT EXISTS {self.__TABLE_NAME__} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) NOT NULL UNIQUE,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES {PlanetModel.__TABLE_NAME__}(name)
            )
        """
        exec_commands([create_table_cmd])

    def list(self):
        ths_tb = self.__TABLE_NAME__
        ref_tb = PlanetModel.__TABLE_NAME__
        cmd = f"""
            SELECT * FROM {ths_tb}
            LEFT JOIN {ref_tb} ON {ths_tb}.homeworld = {ref_tb}.name
            ORDER BY {ref_tb}.climate
        """
        self.cur.execute(cmd)
        rows = self.cur.fetchall()
        self.cur.close()
        return [ dict(r) for r in rows] 