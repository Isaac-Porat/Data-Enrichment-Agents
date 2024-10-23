import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_PATH = os.getenv("CSV_PATH")

def write_column(value, column_name: str, row: int = None):

    df = pd.read_csv(SPREADSHEET_PATH)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")

    if row is None:
        # Write to all rows
        df[column_name] = value

    elif isinstance(row, int):
        # Write to a single row
        df.at[row, column_name] = value

    elif isinstance(row, (list, range, pd.Series)):
        # Write to multiple specified rows
        df.loc[row, column_name] = value

    else:
        raise ValueError("Invalid row specifier. Use int for single row, list/range/Series for multiple rows, or None for all rows.")

    df.to_csv(SPREADSHEET_PATH, index=False)