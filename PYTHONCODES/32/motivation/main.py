import random as rd
import smtplib
from decouple import config
from pathlib import Path
import datetime as dt

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
MY_EMAIL = config("EMAIL_USER")
MY_PASSWORD = config("EMAIL_PASSWORD")
RECEIVER_EMAIL = config("receiver_email")

BASE_DIR = Path(__file__).parent
quotes_file = BASE_DIR / "quotes.txt"
quotes = []
now = dt.datetime.now()
print(now)
if now.weekday() == 1:
    with open(quotes_file) as file:
        quotes = file.readlines()
        quote = rd.choice(quotes)
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Motivational Quote of the Day\n\nQuote of the day: {quote}",
            )
