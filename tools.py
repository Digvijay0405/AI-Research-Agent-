import requests
from bs4 import BeautifulSoup
from ddgs import DDGS


# -------------------------------
# Tool 1 - Search
# -------------------------------
def web_search(query):
    results = []

    try:
        with DDGS() as ddgs:
            search = ddgs.text(query, max_results=5)

            for item in search:
                results.append({
                    "title": item.get("title", ""),
                    "url": item.get("href", ""),
                    "snippet": item.get("body", "")
                })

    except Exception as e:
        print("Search Error:", e)

    return results


# -------------------------------
# Tool 2 - Fetch Webpage
# -------------------------------
def fetch_page(url):

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join(
            p.get_text(strip=True)
            for p in paragraphs[:20]
        )

        return text

    except Exception as e:
        print("Fetch Error:", e)
        return None


# -------------------------------
# Tool 3 - Summarizer
# -------------------------------
def summarize(text, question):

    if not text:
        return "No information available."

    sentences = text.replace("\n", " ").split(". ")

    bullets = []

    for sentence in sentences[:10]:
        if sentence.strip():
            bullets.append("• " + sentence.strip())

    return (
        f"Research Question: {question}\n\n"
        "Summary:\n\n"
        + "\n".join(bullets)
    )