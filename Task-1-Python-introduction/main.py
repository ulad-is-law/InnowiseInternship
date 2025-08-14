from db_conector import Db_connector
from dataloader import Dataloader
from queryrunner import QueryRunner
from resultsaver import ResultSaver


def main():
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
    resultsaver = ResultSaver()

    ouput, columns = qrunner.runsql('sql_queries/query1.sql')
    resultsaver.save_json(ouput, columns, 'json_results/q1_result.json')

    ouput, columns = qrunner.runsql('sql_queries/query2.sql')
    resultsaver.save_json(ouput, columns, 'json_results/q2_result.json')

    ouput, columns = qrunner.runsql('sql_queries/query3.sql')
    resultsaver.save_json(ouput, columns, 'json_results/q3_result.json')

    ouput, columns = qrunner.runsql('sql_queries/query4.sql')
    resultsaver.save_json(ouput, columns, 'json_results/q4_result.json')


main()