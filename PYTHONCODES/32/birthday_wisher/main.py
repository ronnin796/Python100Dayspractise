import random as rd
import smtplib
from decouple import config
from pathlib import Path
import datetime as dt
import pandas as pd

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
MY_EMAIL = config("EMAIL_USER")
MY_PASSWORD = config("EMAIL_PASSWORD")
MY_NAME = config("MY_NAME")

BASE_DIR = Path(__file__).parent
letter_templates = BASE_DIR / "letter_templates"
now = dt.datetime.now()
date_of_birth = (now.month, now.day)
birthdays_file = BASE_DIR / "birthdays.csv"
data = pd.read_csv(birthdays_file)
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
if date_of_birth in birthdays_dict:
    birthday_person = birthdays_dict[date_of_birth]
    file_path = letter_templates / f"letter_{rd.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["names"])
        contents = contents.replace("[MYNAME]", MY_NAME)
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}",
            )
