from db_conector import Db_connector
from dataloader import Dataloader
from queryrunner import QueryRunner
connection = {
"host" : "localhost",
"dbname" : "task1",
"user" : "postgres",
"password" : "8651",
"port" : "5432"
}


conn = Db_connector(connection)
conn.connect()
qrunner = QueryRunner(conn.get_connection())
qrunner.runsql('sql_queries/create_tables.sql')

dl = Dataloader(connection)
#dl.load_file('Jsons/rooms.json', 'rooms')
#dl.load_file('Jsons/students.json', 'students')