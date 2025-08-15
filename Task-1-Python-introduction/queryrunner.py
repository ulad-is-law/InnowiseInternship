import psycopg2


class QueryRunner:
    def __init__(self, connection):
        self.connection = connection

    def runsql(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                sql = f.read()
        except FileNotFoundError:
            print(f"FIle '{filepath}' not found.")
            return None, None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

                if cursor.description:
                    result = cursor.fetchall()
                    column_names = [desc[0] for desc in cursor.description]
                    print(f"query {filepath} ran succesfully")
                    return result, column_names
                else:
                    self.connection.commit()
                    return None, None

        except (Exception, psycopg2.DatabaseError) as e:
            self.connection.rollback()
            print(f"SQL Error: {e}")
            return None, None
