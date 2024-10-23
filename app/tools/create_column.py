import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_PATH = os.getenv("CSV_PATH")

def create_column(column_position: int, column_name: str):
    try:
        df = pd.read_csv(SPREADSHEET_PATH)

        df.insert(loc=column_position, column=column_name, value=" ")

        df.to_csv(SPREADSHEET_PATH, index=False)
        print(f"CSV file successfully updated with {column_name}")

    except ValueError:
        raise ValueError("Could not create column. Use str for column_name and int for column_position")