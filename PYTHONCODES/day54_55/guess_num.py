from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


def makebold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function(*args , **kwargs)}</b>"

    return wrapper


@app.route("/")
def hello_world():
    return """
    <h1 style="color:black;">Guess a number between 0-9.</h1>
    <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTd3cXhvOGk3cnJ1M25lMGx3Zzc3dWljaTFtNjRvNm4zenliaHZsZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pH1swuo2JsnACovyRA/giphy.gif">
    """


@app.route("/<int:number>/")
def check_guess(number):
    if number < random_number:
        return """
        <h1 style="color:blue;">Too Low! Try Again.</h1>
        <p style="color:blue;">The guess is lower. Keep digging.</p>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">
        """

    elif number > random_number:
        return """
        <h1 style="color:red;">Too High! Try Again.</h1>
        <p style="color:red;">The guess is higher than the target.</p>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
        """

    else:
        return """
        <h1 style="color:green;">Correct Guess! 🎉</h1>
        <p style="color:green;">You found the number!</p>
        <img src="https://media.giphy.com/media/111ebonMs90YLu/giphy.gif">
        """


if __name__ == "__main__":
    app.run(debug=True)
