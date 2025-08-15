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
    try:
        conn = Db_connector(connection)
        conn.connect()
        qrunner = QueryRunner(conn.get_connection())
        dl = Dataloader(connection)
        resultsaver = ResultSaver()
        qrunner.runsql("C:/Internship/task1/Task-1-Python-introduction/sql_queries/create_tables.sql")
        qrunner.runsql("C:/Internship/task1/Task-1-Python-introduction/sql_queries/indexes.sql")
        print('Application is opened correctly!')
    except Exception as e:
        print(f'Error during starting application: {e}')
        return
    action = 0
    while action != 3:
        action  = input('print what action you would like to choose: \n 1 - load jsons \n 2 - run queries \n 3 - exit application \n print: ')
        try:
            action = int(action)
        except ValueError:
            print('Incorect choice of action')
            continue
        if action == 1:
            path = input('print the pass to your json:')
            table = input('print table to insert in:')
            dl.load_file(path, table)

        elif action == 2:
            query_path =  input('print the pass to your query:')
            save_path = input('If you want a json to be saved after your query type place and name of the file, if not print: no \n ')
            
            if save_path == 'no':
                qrunner.runsql(query_path)
                continue
            else:
                ouput, columns = qrunner.runsql(query_path)
                resultsaver.save_json(ouput, columns, save_path)

    conn.disconnect()

if __name__ == "__main__":
    main()