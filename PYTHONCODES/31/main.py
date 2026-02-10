BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
from pathlib import Path
import pandas as pd
import random


# ---------------------------- FONT SETUP ------------------------------- #
TITLE_FONT_LANGUAGE = ("Arial", 40, "italic")
LABEL_FONT_WORD = ("Arial", 60, "bold")
ENTRY_FONT = ("Arial", 14, "normal")
BUTTON_FONT = ("Arial", 13, "bold")

BASE_DIR = Path(__file__).parent
screen = tk.Tk()
screen.title("Flash Card App")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ---------------------------- Data ------------------------------- #
data = pd.read_csv(BASE_DIR / "data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = random.choice(to_learn)
# print(to_learn)

# ---------------------------- Image Assets ------------------------------- #
front_image_path = BASE_DIR / "./images/card_front.png"
back_image_path = BASE_DIR / "./images/card_back.png"
front_image = tk.PhotoImage(file=front_image_path)
back_image = tk.PhotoImage(file=back_image_path)


# ---------------------------- Card Flip ------------------------------- #
def countdown():
    screen.after(3000, flip_card)


def flip_card():
    global current_card, canvas_image
    canvas_image = back_image
    canvas.itemconfig(canvas_item, image=canvas_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- Functions ------------------------------- #
def next_card():
    global current_card, canvas_image
    canvas_image = front_image
    canvas.itemconfig(canvas_item, image=canvas_image)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    countdown()


# ---------------------------- UI SETUP ------------------------------- #
canvas = tk.Canvas(
    width=800, height=522, bg="White", highlightthickness=0, background=BACKGROUND_COLOR
)
canvas_image = front_image
canvas_item = canvas.create_image(400, 263, image=canvas_image)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text Objects
language_text = canvas.create_text(
    400, 150, text="French", font=TITLE_FONT_LANGUAGE, fill="black"
)
word_text = canvas.create_text(
    400, 263, text="Word", font=LABEL_FONT_WORD, fill="black"
)

# Buttons
no_button_file = BASE_DIR / "./images/wrong.png"
no_button_image = tk.PhotoImage(file=no_button_file)
no_button = tk.Button(
    screen,
    image=no_button_image,
    highlightthickness=0,
    command=next_card,
)
no_button.grid(row=1, column=0)

yes_button_file = BASE_DIR / "./images/right.png"
yes_button_image = tk.PhotoImage(file=yes_button_file)
yes_button = tk.Button(
    screen,
    image=yes_button_image,
    highlightthickness=0,
    command=next_card,
)
yes_button.grid(row=1, column=1)


countdown()
screen.mainloop()
