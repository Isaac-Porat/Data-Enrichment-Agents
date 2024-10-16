import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_PATH = os.getenv("SPREADSHEET_PATH")

def load_file(filename: str):
    df = pd.read_csv(filename)

    print(df)

if __name__ == "__main__":

    try:
        if not os.path.exists(SPREADSHEET_PATH):
            raise FileNotFoundError(f"File not found: {SPREADSHEET_PATH}")
        load_file(SPREADSHEET_PATH)
    except FileNotFoundError as e:
        raise ValueError(str(e))

