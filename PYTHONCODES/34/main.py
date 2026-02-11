from question_model import Question
from data import get_data
from quiz_brain import QuizBrain

question_data = get_data()
print(question_data)
question_bank = [
    Question(question["question"], question["answer"]) for question in question_data
]

quiz = QuizBrain(question_bank)

for question in question_bank:
    print(question.text)

BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
from pathlib import Path
import random


# ---------------------------- FONT SETUP ------------------------------- #
TITLE_FONT_LANGUAGE = ("Arial", 25, "italic")
LABEL_FONT_WORD = ("Arial", 60, "bold")
ENTRY_FONT = ("Arial", 14, "normal")
BUTTON_FONT = ("Arial", 13, "bold")

BASE_DIR = Path(__file__).parent
screen = tk.Tk()
screen.title("Quizzler App")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# ---------------------------- Data ------------------------------- #
def check_answer(answer):
    if quiz.check_answer(answer):
        canvas.config(bg="green")
        canvas.itemconfig(score_text, text=f"Score: {quiz.score}")
    else:
        canvas.config(bg="red")
    screen.after(1000, next_card)


def next_card():

    canvas.config(bg=BACKGROUND_COLOR)
    if quiz.still_has_questions():
        quiz.next_question()
        current_question = quiz.current_question.text
        canvas.itemconfig(question_text, text=current_question)
    else:
        canvas.itemconfig(question_text, text="You've reached the end of the quiz.")


# -------------- UI SETUP ------------------------------- #
canvas = tk.Canvas(
    width=800,
    height=522,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    background=BACKGROUND_COLOR,
)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text Objects
question_text = canvas.create_text(
    400,
    150,
    text="Welcome to the Quiz!",
    font=TITLE_FONT_LANGUAGE,
    fill="black",
    width=300,
)

# Score Text Object
score_text = canvas.create_text(
    700, 20, text=f"Score: {quiz.score}", font=BUTTON_FONT, fill="black", anchor="e"
)
next_card()

# Buttons
no_button_file = BASE_DIR / "./images/false.png"
no_button_image = tk.PhotoImage(file=no_button_file)
no_button = tk.Button(
    screen,
    image=no_button_image,
    highlightthickness=0,
    command=lambda: check_answer("False"),
)
no_button.grid(row=1, column=0)

yes_button_file = BASE_DIR / "./images/true.png"
yes_button_image = tk.PhotoImage(file=yes_button_file)
yes_button = tk.Button(
    screen,
    image=yes_button_image,
    highlightthickness=0,
    command=lambda: check_answer("True"),
)
yes_button.grid(row=1, column=1)


screen.mainloop()
