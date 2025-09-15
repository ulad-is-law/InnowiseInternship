from python_db_package.db_initializer import Db_initializer
from python_db_package.dataloader import Dataloader
from python_db_package.queryrunner import QueryRunner
from python_db_package.resultsaver import ResultSaver
from python_db_package.db_conector import Db_connector
from dotenv import load_dotenv
from pathlib import Path
import os


def console_application_loop(
    dl: Dataloader, qrunner: QueryRunner, resultsaver: ResultSaver
):
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

        if action == 1:  # load jsons
            directory_path = Path("task1_py_intro/raw_data")

            print("\n--- Load JSON File ---")

            if directory_path.is_dir():
                print("Available files in the default directory:")
                available_files = [
                    f.name for f in directory_path.iterdir() if f.is_file()
                ]
                if available_files:
                    for file_name in available_files:
                        print(f"  - {file_name}")
                else:
                    print("  (No files found)")
            else:
                print(f"Warning: Default directory not found at '{directory_path}'")

            prompt = (
                "\nEnter the name of a file from the list above,\n"
                "OR enter a full, absolute path to another JSON file,\n"
                "OR type '3' to cancel: "
            )
            file_choice = input(prompt)

            if file_choice == "3":
                continue

            path_to_load = Path(file_choice)

            if not path_to_load.is_absolute():
                path_to_load = directory_path / path_to_load

            if not path_to_load.is_file():
                print(f"\nError: File not found at '{path_to_load}'")
                continue

            table = input("Enter the table name to insert data into: ")
            dl.load_file(str(path_to_load), table)

        """query_path = input("print the pass to your query:")
            save_path = input(
                "If you want a json to be saved after your query type place and name of the file, if not print: no \n "
            )

            if save_path == "no":
                qrunner.runsql(query_path)
                continue
            else:
                ouput, columns = qrunner.runsql(query_path)
                resultsaver.save_json(ouput, columns, save_path)
                    """
        if action == 2:
            sql_dir = Path(r"task1_py_intro\sql_queries")
            results_dir = Path("task1_py_intro/json_results")

            print("\n--- Run SQL Query ---")

            if sql_dir.is_dir():
                print("Available SQL files in default directory:")
                available_files = [f.name for f in sql_dir.iterdir() if f.is_file()]
                if available_files:
                    for file_name in available_files:
                        print(f"  - {file_name}")
                else:
                    print("  (No files found)")
            else:
                print(f"Warning: Default SQL directory not found at '{sql_dir}'")

            prompt = (
                "\nEnter the name of a file from the list above,\n"
                "OR enter a full, absolute path to another SQL file,\n"
                "OR type 'cancel' to return to the main menu: "
            )
            file_choice = input(prompt)

            if file_choice.lower() == "cancel":
                continue

            query_path = Path(file_choice)
            if not query_path.is_absolute():
                query_path = sql_dir / query_path

            if not query_path.is_file():
                print(f"\nError: SQL file not found at '{query_path}'")
                continue

            save_prompt = (
                "\nTo save results, provide a full path (e.g., C:\\data\\res.json)\n"
                "OR just a filename to save in the default folder (e.g., results.json).\n"
                "Type 'no' to run the query without saving: "
            )
            save_path_input = input(save_prompt)

            output, columns = qrunner.runsql(str(query_path))

            if save_path_input.lower() != "no":
                if output is not None:
                    save_path = Path(save_path_input)
                    if not save_path.is_absolute():
                        save_path = results_dir / save_path

                    save_path.parent.mkdir(parents=True, exist_ok=True)
                    resultsaver.save_json(output, columns, str(save_path))


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
        r"task1_py_intro/sql_init_queries/create_tables.sql",
        r"task1_py_intro/sql_init_queries/indexes.sql",
    ]

    initializer = Db_initializer(connection, db_init_sql_files)
    if not initializer.initialize():
        print("Application shutting down due to initialization failure.")
        return
    try:
        conn = Db_connector(connection)
        conn.connect()
        qrunner = QueryRunner(conn.get_connection())
        dl = Dataloader(connection)
        resultsaver = ResultSaver()
        print("Application is ready to use!")
    except Exception as e:
        print(f"Error during application setup: {e}")
        conn.disconnect()
        return

    action = 0

    console_application_loop(dl, qrunner, resultsaver)

    conn.disconnect()


if __name__ == "__main__":
    main()
