import os
import requests
from urllib.parse import urlparse
from googlesearch import search
from tqdm import tqdm

def download_pdf(url, output_folder):
    try:
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        filepath = os.path.join(output_folder, filename)

        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✅ Downloaded: {filename}")
        else:
            print(f"⚠️ Skipped (Not a PDF or failed): {url}")
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")

def scrape_pdfs(query, num_results=10, output_folder="downloaded_pdfs"):
    os.makedirs(output_folder, exist_ok=True)
    search_query = f"{query} filetype:pdf"

    print(f"🔍 Searching for PDFs with query: '{search_query}'")
    results = list(search(search_query, num_results=num_results))

    for url in tqdm(results, desc="Downloading PDFs"):
        if url.lower().endswith(".pdf"):
            download_pdf(url, output_folder)

if __name__ == "__main__":
    # Customize your query here
    topics = [
        "invoice sample",
        "business contract",
        "academic paper site:arxiv.org",
        "government form site:.gov"
    ]

    for topic in topics:
        folder_name = topic.split()[0].replace(":", "")
        scrape_pdfs(topic, num_results=10, output_folder=f"src/data/processed/{folder_name}")
