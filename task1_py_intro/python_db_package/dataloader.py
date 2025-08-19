import pandas as pd
from sqlalchemy import create_engine


class Dataloader:

    SCHEMAS = {
        "students": {
            "birthday": {"dtype": "datetime64[ns]", "nullable": False},
            "id": {"dtype": "int64", "nullable": False},
            "name": {"dtype": "string", "nullable": False},
            "room": {"dtype": "int64", "nullable": False},
            "sex": {"dtype": "string", "nullable": False},
        },
        "rooms": {
            "id": {"dtype": "int64", "nullable": False},
            "name": {"dtype": "object", "nullable": False},
        },
    }

    def __init__(self, connection: dict):
        self.connection = connection

        connection_string = (
            f"postgresql+psycopg2://{self.connection['user']}:{self.connection['password']}"
            f"@{self.connection['host']}:{self.connection['port']}/{self.connection['dbname']}"
        )
        self.engine = create_engine(connection_string)

    def is_valid_file(
        self, target_schema: str, filepath: str
    ) -> tuple[bool, pd.DataFrame | None]:
        try:
            df = pd.read_json(filepath, dtype=False)
            if df.empty:
                return False, False
        except Exception as e:
            print(f"Error: {e}")
            return False, None

        if set(df.columns) != set(target_schema.keys()):
            return False, None

        for col_name, rules in target_schema.items():
            if not rules["nullable"] and df[col_name].isnull().any():
                return False, None
            try:
                df[col_name].astype(rules["dtype"])
            except Exception:
                return False, None

        return True, df

    def load_file(self, filepath: str, table: str):
        if table not in self.SCHEMAS:
            print(f"There is no table {table} in database")
            return
        is_valid, df = self.is_valid_file(self.SCHEMAS[table], filepath)
        if not is_valid:
            print("validation error")
            return
        try:
            df.to_sql(table, self.engine, if_exists="append", index=False)
            print(f"{table} json was inserted succesfully")
        except Exception as e:
            print(f"Error during inserting! {e}")
