import random as rd
import smtplib
from decouple import config
from pathlib import Path
import datetime as dt

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
MY_EMAIL = config("EMAIL_USER")
MY_PASSWORD = config("EMAIL_PASSWORD")
RECEIVER_EMAIL = config("RECEIVER_EMAIL")

BASE_DIR = Path(__file__).parent


now = dt.datetime.now()


def send_mail(subject: str, body: str) -> None:
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:{subject}\n\n{body}",
        )
