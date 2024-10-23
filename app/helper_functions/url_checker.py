import os
import pandas as pd
from dotenv import load_dotenv
import validators
from urllib.parse import urlparse

load_dotenv()

SPREADSHEET_PATH = os.getenv("CSV_PATH")

def validate_url(url: str) -> bool:
    try:
        result = urlparse(url)

        # Check to see if valid URL with scheme and netloc (domain)
        if result.scheme and result.netloc:
            validation = validators.url(url) # validators package for stricter validation
            if validation:
                return True

        # If not valid URl, check if it's a valid path
        elif result.path:
            if result.path.startswith("/") and " " not in result.path:
                return True

        return False

    except Exception:
        return False

def loop_through_csv():
    try:
        df = pd.read_csv(SPREADSHEET_PATH)

        for index, row in df.iterrows():
            value = row["Company URL"]

            if validate_url(value):
                print(value)
            else:
                df.at[index, "Company URL"] = f"https://{value}"

        df.to_csv(SPREADSHEET_PATH, index=False)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    loop_through_csv()