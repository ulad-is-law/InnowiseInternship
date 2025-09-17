import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

db_params = {
        "host": os.getenv("DB_HOST"),
        "dbname": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "port": os.getenv("POSTGRES_PORT"),
    }


conn = psycopg2.connect(**db_params)

cursor = conn.cursor()

with open('create_table.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
    
conn.commit()
def load_data(file_path: str) -> pd.DataFrame:
    try:
        raw_df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error, file not found on the path: {file_path}")
        return pd.DataFrame()
    return raw_df

raw_df = load_data('task_2_data_ex.xlsx')
