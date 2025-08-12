import psycopg2

class QueryRunner:
    def __init__(self, connection):
        self.connection = connection

    def runsql(self, filepath):
        try:
            with open(filepath, "r") as f:
                sql = f.read()
        except FileNotFoundError:
            print(f"Error: The file at '{filepath}' was not found.")

        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

