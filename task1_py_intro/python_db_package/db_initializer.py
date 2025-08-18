from .db_conector import Db_connector
from .queryrunner import QueryRunner

class Db_initializer:

    def __init__(self, connection_details: dict, sql_files: list):
        self.connection_details = connection_details
        self.sql_files = sql_files
        

    def initialize(self):
        try:
            conn = Db_connector(self.connection_details)
            conn.connect()
            qrunner = QueryRunner(conn.get_connection())
            for i in self.sql_files:
                if not qrunner.runsql(i):
                    print(f"Error during db initialization: init file not found")
                    raise
            
            print("Db is initialized correctly!")
        except Exception as e:
            print(f"Error during db initialization: {e}")
            conn.disconnect()
            raise
        