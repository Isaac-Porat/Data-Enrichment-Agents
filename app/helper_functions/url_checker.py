import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_PATH = os.getenv("CSV_PATH")

def url_checker():
    try:
        df = pd.read_csv(SPREADSHEET_PATH)

        for index, row in df.iterrows():
            value = row["Company URL"]

            df.at[index, "Company URL"] = f"https://{value}"

        df.to_csv(SPREADSHEET_PATH, index=False)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    url_checker()