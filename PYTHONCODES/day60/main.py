from flask import Flask, render_template, request
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST.

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        name = request.form.get("name")
        password = request.form.get("password")
        return render_template("login.html", name=name, password=password)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
