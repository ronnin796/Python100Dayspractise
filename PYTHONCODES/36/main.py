import requests
from decouple import config
from twilio_msg import send_message

# ==============================
# CONFIG
# ==============================

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_THRESHOLD = 2  # percent

ALPHAVANTAGE_API_KEY = config("ALPHAVANTAGE_KEY")
NEWS_API_KEY = config("NEWS_API_KEY")

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"


# ==============================
# STOCK LOGIC
# ==============================


def get_stock_percentage_change():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": ALPHAVANTAGE_API_KEY,
    }

    response = requests.get(STOCK_URL, params=params)
    response.raise_for_status()

    data = response.json()
    time_series = data["Time Series (Daily)"]

    # Sort dates newest → oldest
    dates = sorted(time_series.keys(), reverse=True)

    yesterday_close = float(time_series[dates[0]]["4. close"])
    day_before_close = float(time_series[dates[1]]["4. close"])

    difference = yesterday_close - day_before_close
    percentage_change = (difference / day_before_close) * 100

    return percentage_change


# ==============================
# NEWS LOGIC
# ==============================


def get_news_articles():
    params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3,
    }

    response = requests.get(NEWS_URL, params=params)
    response.raise_for_status()

    return response.json()["articles"]


# ==============================
# MESSAGE FORMATTING
# ==============================


def format_messages(percentage_change, articles):
    arrow = "🔺" if percentage_change > 0 else "🔻"

    messages = []

    for article in articles:
        message = (
            f"{STOCK}: {arrow}{abs(percentage_change):.2f}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )
        messages.append(message)

    return messages


# ==============================
# MAIN EXECUTION
# ==============================


def main():
    percentage_change = get_stock_percentage_change()

    print(f"Stock change: {percentage_change:.2f}%")

    if abs(percentage_change) >= STOCK_THRESHOLD:
        articles = get_news_articles()
        messages = format_messages(percentage_change, articles)

        for msg in messages:
            send_message(msg)


if __name__ == "__main__":
    main()
