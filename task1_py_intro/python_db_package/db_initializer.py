from .db_conector import Db_connector
from .queryrunner import QueryRunner


class Db_initializer:

    def __init__(self, connection_details: dict, sql_files: list):
        self.connection_details = connection_details
        self.sql_files = sql_files

    def initialize(self) -> bool:
        print("Starting database initialization...")
        db_conn = None
        try:
            db_conn = Db_connector(self.connection_details)
            db_conn.connect()

            qrunner = QueryRunner(db_conn.get_connection())

            print("Running SQL setup scripts...")
            for script_path in self.sql_files:
                print(f"  Executing: {script_path}")
                qrunner.runsql(script_path)

            print("Database initialized successfully!")
            return True

        except Exception as e:
            print(f"FATAL: Database initialization failed: {e}")
            return False

        finally:
            if db_conn:
                db_conn.disconnect()
