from db_conector import Db_connector
from dataloader import Dataloader
from queryrunner import QueryRunner
from resultsaver import ResultSaver
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
test_ouput, columns = qrunner.runsql('sql_queries/test.sql')

print(test_ouput, columns)
print('---------------------------------------------')
resultsaver = ResultSaver()
resultsaver.save_json(test_ouput, columns, 'json_results/test.json')