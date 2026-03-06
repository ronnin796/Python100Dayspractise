from flask import Flask

app = Flask(__name__)


def makebold(function):
    def wrapper():
        return f"<b> {function()} </b>"

    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/path")
@makebold
def different_path():
    return "<p>This is a differet path </p>"


if __name__ == "__main__":
    app.run(debug=True)
