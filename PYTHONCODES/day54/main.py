from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/path")
def different_path():
    return "<p>This is a differet path </p>"


if __name__ == "__main__":
    app.run()
