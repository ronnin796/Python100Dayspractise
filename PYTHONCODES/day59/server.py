from flask import Flask, render_template
from datetime import date, datetime
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts")
def get_post():
    return render_template("post.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Example decorator
def makebold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


@app.route("/bold")
@makebold
def bold_text():
    return "This text is bolded using a decorator!"


if __name__ == "__main__":
    app.run(debug=True)
