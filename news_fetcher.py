import requests
from config import NEWS_API_KEY

NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_news(stock_ticker):
    params = {
        'q': stock_ticker,
        'apiKey': NEWS_API_KEY,
        'language': 'en'
    }
    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code != 200:
        print("Error fetching news:", response.status_code)
        return []

    data = response.json()
    articles = [article['title'] for article in data.get('articles', [])]

    return articles
