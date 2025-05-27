import requests
from bs4 import BeautifulSoup
import tldextract

def get_webpage_text(url: str) -> str:
    """
    Fetch and extract clean text content from a web page.

    Parameters:
        url (str): The web URL to extract content from.

    Returns:
        str: The main visible text content of the page.
    """
    # Validate the URL
    extracted = tldextract.extract(url)
    if not extracted.domain or not extracted.suffix:
        raise ValueError("Invalid URL format")

    # Fetch HTML content
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    # Parse and clean text
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=' ')
    clean_text = ' '.join(text.split())
    
    if not clean_text or len(clean_text) < 100:
        raise ValueError("Extracted content is too short or empty.")
    
    return clean_text
