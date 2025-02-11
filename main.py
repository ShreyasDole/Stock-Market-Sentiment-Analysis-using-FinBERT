from news_fetcher import fetch_news
from sentiment_model import analyze_sentiment

def main():
    stock_ticker = input("Enter stock ticker (e.g., RELIANCE, TCS, INFY): ").upper()

    # Fetch news articles related to the stock
    news_articles = fetch_news(stock_ticker)

    if not news_articles:
        print("No news found for the given stock.")
        return

    print("\n🔍 Analyzing Sentiment of News Articles...\n")

    # Analyze sentiment for each article
    for idx, article in enumerate(news_articles[:5], 1):  # Limit to 5 articles
        sentiment_result = analyze_sentiment(article)
        print(f"{idx}. {sentiment_result['text']}")
        print(f"   ➤ Sentiment: {sentiment_result['sentiment']} (Confidence: {sentiment_result['confidence']})\n")

if __name__ == "__main__":
    main()
