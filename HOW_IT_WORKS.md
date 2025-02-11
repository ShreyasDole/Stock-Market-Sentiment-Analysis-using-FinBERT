### 📜 `HOW_IT_WORKS.md`  


# 🧐 How It Works – Stock Market Sentiment Analysis  

This document explains **how the project works**, including:  
✅ How we fetch stock news using **NewsAPI**  
✅ How we analyze sentiment using **FinBERT**  
✅ How data flows between different Python files  

---

## 📌 1️⃣ Fetching Stock Market News  

📍 **File:** `news_fetcher.py`  
📍 **Purpose:** Fetches real-time stock market news using **NewsAPI**  

### **🔹 Steps:**  
1. Calls **NewsAPI** to get the latest stock-related articles  
2. Filters and extracts **headlines**  
3. Returns a **list of headlines** for analysis  

### **🔹 Code Breakdown:**  
```python
import requests
from config import NEWS_API_KEY

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=stocks&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract only the headlines
    headlines = [article["title"] for article in data.get("articles", [])]
    return headlines
```
✔ Uses `requests.get()` to fetch news  
✔ Extracts **only the headlines** from JSON response  
✔ Returns a list of stock-related news titles  

---

## 📌 2️⃣ Sentiment Analysis with FinBERT  

📍 **File:** `sentiment_model.py`  
📍 **Purpose:** Analyzes sentiment of stock news headlines using **FinBERT**  

### **🔹 Steps:**  
1. Loads **FinBERT model**  
2. Tokenizes each news headline into **numerical inputs**  
3. Runs the input through FinBERT to predict **sentiment scores**  
4. Returns **Positive, Negative, or Neutral** classification  

### **🔹 Code Breakdown:**  
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load FinBERT Model
model_name = "ProsusAI/finbert"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def analyze_sentiment(news_headline):
    inputs = tokenizer(news_headline, return_tensors="pt", truncation=True)
    output = model(**inputs)

    # Apply softmax to get probabilities
    sentiment_scores = torch.nn.functional.softmax(output.logits, dim=-1)
    labels = ["Negative", "Neutral", "Positive"]
    
    # Get the sentiment with the highest score
    sentiment = labels[sentiment_scores.argmax()]
    confidence = round(sentiment_scores.max().item() * 100, 2)

    return sentiment, confidence
```
✔ Loads **FinBERT** for financial text analysis  
✔ Converts text into **numerical tokens** for the model  
✔ Predicts sentiment and returns **confidence score**  

---

## 📌 3️⃣ Running the Main Program  

📍 **File:** `main.py`  
📍 **Purpose:** Ties everything together – fetches news, analyzes sentiment, and prints results  

### **🔹 Steps:**  
1. Calls `fetch_news()` to get stock-related headlines  
2. Passes each headline to `analyze_sentiment()`  
3. Prints the **sentiment result & confidence score**  

### **🔹 Code Breakdown:**  
```python
from news_fetcher import fetch_news
from sentiment_model import analyze_sentiment

def main():
    print("Fetching latest stock market news...\n")
    headlines = fetch_news()

    for idx, headline in enumerate(headlines[:5]):  # Process first 5 headlines
        sentiment, confidence = analyze_sentiment(headline)
        print(f"{idx+1}. \"{headline}\"\n   Sentiment: {sentiment} ({confidence}%)\n")

if __name__ == "__main__":
    main()
```
✔ Calls **fetch_news()** to get stock headlines  
✔ Calls **analyze_sentiment()** on each headline  
✔ Prints **Positive, Negative, or Neutral** result  

---

## 📌 4️⃣ Full Project Flow  

1️⃣ **User runs `main.py`**  
2️⃣ `main.py` calls **`fetch_news()`** (gets stock news)  
3️⃣ Each news headline is sent to **`analyze_sentiment()`**  
4️⃣ **FinBERT predicts sentiment** and returns confidence score  
5️⃣ Final result is displayed to the user  

**Example Output:**  
```sh
Fetching latest stock market news...

1️⃣ "Stock market sees massive gains as tech sector surges."
   Sentiment: Positive (85%)  

2️⃣ "Investors worried as inflation concerns rise."
   Sentiment: Negative (78%)  

3️⃣ "Oil prices remain stable amid global uncertainties."
   Sentiment: Neutral (67%)  
```

---

## ✅ Summary  

📌 `news_fetcher.py` → **Fetches stock news** from NewsAPI  
📌 `sentiment_model.py` → **Uses FinBERT to analyze sentiment**  
📌 `main.py` → **Runs the program & displays results**  

---
