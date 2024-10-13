from psycopg2.extras import RealDictCursor

from . import connect, exec_commands

# Create your models here.
class MovieModel:
    __TABLE_NAME__ = "ex02_movies"

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
                release_date DATE NOT NULL
            )
        """
        exec_commands([create_table_cmd])

    def bulk_insert(self, data: list):
        fields = list(data[0].keys())
        results = []
        for d in data:
            print(d)
            cmd = f"INSERT INTO {self.__TABLE_NAME__} ({','.join(fields)}) VALUES {tuple(d.values())}"
            try:
                self.cur.execute(cmd)
                results.append({'title': d['title'], 'status': True, 'message': 'OK'})
            except Exception as e:
                results.append({'title': d['title'], 'status': False, 'message': str(e)})
            self.conn.commit()
        return results
    
    def list(self):
        try:
            self.cur.execute(f"SELECT * FROM {self.__TABLE_NAME__}")
            rows = self.cur.fetchall()
            self.cur.close()
            return [ dict(r) for r in rows]
        except Exception as e:
            print(e)
            return []