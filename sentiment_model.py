from transformers import pipeline

# Load FinBERT model for sentiment analysis
sentiment_pipeline = pipeline("text-classification", model="ProsusAI/finbert")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return {'text': text, 'sentiment': result['label'], 'confidence': round(result['score'], 2)}
