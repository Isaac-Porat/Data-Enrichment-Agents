import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_PATH = os.getenv("CSV_PATH")

def read_column(column_name: str, row: int):
    try:
        df = pd.read_csv(SPREADSHEET_PATH)

        return df.loc[row, column_name]

    except ValueError:
        raise ValueError("Row and column value not found. Use int for single row and str for column_name.")