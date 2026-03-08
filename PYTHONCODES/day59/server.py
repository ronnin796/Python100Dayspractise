from flask import Flask, render_template
from datetime import date, datetime
import requests
from flask import abort

app = Flask(__name__)


def get_blog():
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url)
    blogs = response.json()

    return blogs


@app.route("/")
def index():
    responses = get_blog()
    return render_template("index.html", blogs=responses)


@app.route("/posts")
def get_posts():
    return render_template("posts.html")


@app.route("/post/<int:id>")
def get_post(id):
    blogs = get_blog()
    post = next((post for post in blogs if post["id"] == id), None)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)


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
