from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user, login_required
import random as rd
import smtplib
from decouple import config
from pathlib import Path
import datetime as dt


def admin_required(f):
    @wraps(f)
    @login_required  # ensures the user is logged in first
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash("You are not authorized to access this page.", "danger")
            return redirect(url_for("blog.get_all_posts"))
        return f(*args, **kwargs)

    return decorated_function


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
