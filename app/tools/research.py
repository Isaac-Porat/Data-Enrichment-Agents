import os
from dotenv import load_dotenv
from llama_index.readers.web import FireCrawlWebReader
from langchain_community.document_loaders import SitemapLoader

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

def scrape_website(url: str):

    search_urls = []

    try:
        sitemap_loader = SitemapLoader(web_path=url)

        docs = sitemap_loader.load()

        search_urls.append(docs)

    except Exception as e:
        print(str(e))

    data = []

    try:

        for url in search_urls:
            firecrawl_reader = FireCrawlWebReader(
                api_key=FIRECRAWL_API_KEY,
                mode="scrape"            )

            documents = firecrawl_reader.load_data(url=url)

            data.append(documents)

    except Exception as e:
        print(str(e))

    # TODO Load all data or extract description?

    return data