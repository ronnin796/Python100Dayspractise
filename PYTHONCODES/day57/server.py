from flask import Flask, render_template
from datetime import date, datetime
import requests

URL_AGE = "https://api.agify.io/"
URL_GENDER = "https://api.genderize.io/"


def get_age_gender(params: dict) -> list:
    age_response = requests.get(URL_AGE, params=params)
    gender_response = requests.get(URL_GENDER, params=params)
    age = age_response.json()["age"]
    gender = gender_response.json()["gender"]

    return [age, gender]


app = Flask(__name__)


# Example decorator
def makebold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


@app.route("/<name>")
def home(name):

    CURRENT_YEAR = datetime.now().year
    MY_NAME = name.title()
    params = {"name": MY_NAME}
    data = get_age_gender(params)

    return render_template(
        "index.html",
        current_year=CURRENT_YEAR,
        my_name=MY_NAME,
        age=data[0],
        gender=data[1],
    )


@app.route("/blogs/", defaults={"id": None})
@app.route("/blogs/<int:id>")
def get_blog(id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    blogs = response.json()

    return render_template("blogs.html", posts=blogs, id=id)


# Test decorator route
@app.route("/bold")
@makebold
def bold_text():
    return "This text is bolded using a decorator!"


if __name__ == "__main__":
    app.run(debug=True)
