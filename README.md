# 📊 Stock Market Sentiment Analysis using FinBERT  

This project **fetches stock market news** and analyzes the sentiment (**Positive, Negative, Neutral**) using **FinBERT**, a model fine-tuned for financial text sentiment analysis.  

---

## 🚀 Features  
✅ Fetches **real-time stock news** using the **NewsAPI**.  
✅ Uses **FinBERT** to classify the sentiment of news articles.  
✅ Provides **confidence scores** for sentiment predictions.  
✅ Easy-to-use **command-line interface**.  

---

## 🛠️ Installation  

### **1️⃣ Clone the repository**  
```sh
git clone https://github.com/shreyy2005/stock_sentiment_analysis.git
cd stock_sentiment_analysis
```

### **2️⃣ Install Dependencies**  
You need Python **3.8+**. Install required libraries using:  
```sh
pip install -r requirements.txt
```

### **3️⃣ Get News API Key**  
This project requires **NewsAPI** to fetch stock-related news. Follow these steps to get an API key:  

1. Go to **[NewsAPI](https://newsapi.org/register)** and sign up.  
2. After signing up, go to the **API Keys** section and copy your key.  
3. Create a **config.py** file in your project directory and add:  
   ```python
   NEWS_API_KEY = "your_news_api_key_here"
   ```
   ⚠️ **Never share your API key!** Do NOT upload `config.py` to GitHub.

---

## 📜 Usage  

Run the program using:  
```sh
python main.py
```

The script will:  
1. Fetch **latest stock-related news**.  
2. Use **FinBERT** to analyze the sentiment of each news headline.  
3. Display the sentiment classification (**Positive, Negative, or Neutral**) along with **confidence scores**.  

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

## 🏗️ Project Structure  

```
stock_sentiment_analysis/
│── .gitignore             # Ignore sensitive files  
│── LICENSE                # License for open-source use  
│── README.md              # Project documentation  
│── requirements.txt       # Dependencies list  
│── config.py              # Stores API key (DO NOT UPLOAD)  
│── news_fetcher.py        # Fetches stock news  
│── sentiment_model.py     # Loads FinBERT & performs sentiment analysis  
│── main.py                # Runs the program  
└── assets/                # Folder for images used in README (optional)  
```

---

## 📦 Dependencies  
This project uses:  
- **FinBERT** (financial sentiment analysis model)  
- **Requests** (fetch news from API)  
- **Transformers** (load FinBERT model)  
- **Torch** (for deep learning operations)  

To install all dependencies:  
```sh
pip install -r requirements.txt
```


---

## ✨ Contribution  
Feel free to contribute! Open an issue or submit a pull request if you have improvements.

---

## 📢 Support  
If you have any questions, open an issue or reach out at **doleshreyaas117@gmail.com**.

---
