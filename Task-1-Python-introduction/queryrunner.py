import psycopg2

class QueryRunner:
    def __init__(self, connection):
        self.connection = connection

    def runsql(self, filepath):
        try:
            with open(filepath, "r", encoding='utf-8') as f:
                sql = f.read()
        except FileNotFoundError:
            print(f"Ошибка: Файл '{filepath}' не найден.")
            return

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                
                if cursor.description:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
                    return None

        except (Exception, psycopg2.DatabaseError) as e:
            self.connection.rollback()
            print(f"SQL Error: {e}")
            return None
