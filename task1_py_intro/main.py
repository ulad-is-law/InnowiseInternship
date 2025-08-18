from python_db_package.db_initializer import Db_initializer
from python_db_package.dataloader import Dataloader
from python_db_package.queryrunner import QueryRunner
from python_db_package.resultsaver import ResultSaver
from python_db_package.db_conector import Db_connector
from dotenv import load_dotenv
import os


def main():

    load_dotenv()
    
    connection = {
        "host": os.getenv("DB_HOST"),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "port": os.getenv("DB_PORT"),
    }

    db_init_sql_files = [
        r"sql_init_queries/create_tables.sql",
        r"sql_init_queries/indexes.sql"
    ]

    initializer = Db_initializer(connection, db_init_sql_files)
    db_connector_object = initializer.initialize()
    if not db_connector_object:
        return
    try:
        conn = db_connector_object.get_connection()
        qrunner = QueryRunner(conn.db.get_connection())
        dl = Dataloader(connection)
        resultsaver = ResultSaver()
        print("Application is ready to use!")
    except Exception as e:
        print(f"Error during application setup: {e}")
        conn.disconnect()
        return
    action = 0

    while action != 3:
  
        action = input(
            "print what action you would like to choose: \n 1 - load jsons \n 2 - run queries \n 3 - exit application \n print: "
        )
        try:
            action = int(action)
        except ValueError:
            print("Incorect choice of action")
            continue
        if action == 1:
            path = input("print the pass to your json:")
            table = input("print table to insert in:")
            dl.load_file(path, table)

        elif action == 2:
            query_path = input("print the pass to your query:")
            save_path = input(
                "If you want a json to be saved after your query type place and name of the file, if not print: no \n "
            )

            if save_path == "no":
                qrunner.runsql(query_path)
                continue
            else:
                ouput, columns = qrunner.runsql(query_path)
                resultsaver.save_json(ouput, columns, save_path)

    conn.disconnect()


if __name__ == "__main__":
    main()
