import os
import pandas as pd
from pandas import Series
from dotenv import load_dotenv
from llama_index.readers.web import FireCrawlWebReader
from langchain_community.document_loaders import SitemapLoader

load_dotenv()

SPREADSHEET_PATH = os.getenv("SPREADSHEET_PATH")

def load_file(filename: str):
    df = pd.read_csv(filename)

    return df

def extract_company_url(row: Series):
    return row.get("Company URL")

def sitemap_loader(url: str):
    try:
        sitemap_loader = SitemapLoader(web_path=url)

        docs = sitemap_loader.load()

        if len(docs) == 0:
            return url

        return docs

    except Exception as e:
        print(str(e))

def scrape_website(url: str):
    firecrawl_reader = FireCrawlWebReader(
        api_key="fc-7be55bc318be4ac799740f811e0a8fcb",
        mode="scrape"
    )

    documents = firecrawl_reader.load_data(url=url)

    # TODO Load all data or extract description?

    return documents

if __name__ == "__main__":

    try:
        if not os.path.exists(SPREADSHEET_PATH):
            raise FileNotFoundError(f"File not found: {SPREADSHEET_PATH}")
        load_file(SPREADSHEET_PATH)
    except FileNotFoundError as e:
        raise ValueError(str(e))
