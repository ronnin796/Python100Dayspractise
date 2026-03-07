from flask import Flask, render_template

app = Flask(__name__)


def makebold(function):
    def wrapper():
        return f"<b> {function()} </b>"

    return wrapper


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
