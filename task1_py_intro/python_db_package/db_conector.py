import psycopg2


class Db_connector:
    def __init__(self, db_params: dict):
        self.db_params = db_params
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(**self.db_params)
            print("connected succesfully")
        else:
            print("")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("connection closed")
        else:
            print("There is no conection to close")

    def get_connection(self) -> dict:
        return self.connection
