from db_conector import Db_connector

connection = {
"host" : "localhost",
"dbname" : "task1",
"user" : "postgres",
"password" : "8651",
"port" : "5432"
}


conn = Db_connector(connection)
conn.connect()