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
notifcation_message = "Look up! The ISS is above you in the sky."


def send_notification():
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:ISS Overhead Notification\n\n{notifcation_message}",
        )
