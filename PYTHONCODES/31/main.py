BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
from tkinter import messagebox
from pathlib import Path


# ---------------------------- FONT SETUP ------------------------------- #
TITLE_FONT_LANGUAGE = ("Arial", 40, "italic")
LABEL_FONT_WORD = ("Arial", 60, "bold")
ENTRY_FONT = ("Arial", 14, "normal")
BUTTON_FONT = ("Arial", 13, "bold")

BASE_DIR = Path(__file__).parent
screen = tk.Tk()
screen.title("Flash Card App")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# ---------------------------- UI SETUP ------------------------------- #
canvas = tk.Canvas(width=800, height=522, bg="White", highlightthickness=0)
front_image = BASE_DIR / "./images/card_front.png"
canvas_image = tk.PhotoImage(file=front_image)
canvas.create_image(400, 263, image=canvas_image)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
no_button_file = BASE_DIR / "./images/wrong.png"
no_button_image = tk.PhotoImage(file=no_button_file)
no_button = tk.Button(
    screen,
    image=no_button_image,
    highlightthickness=0,
    command=lambda: print("No"),
)
no_button.grid(row=1, column=0)

yes_button_file = BASE_DIR / "./images/right.png"
yes_button_image = tk.PhotoImage(file=yes_button_file)
yes_button = tk.Button(
    screen,
    image=yes_button_image,
    highlightthickness=0,
    command=lambda: print("Yes"),
)
yes_button.grid(row=1, column=1)

# Texts
text_x = 400

language_label = tk.Label(screen, text="French", font=TITLE_FONT_LANGUAGE, bg="White")
language_label.place(x=text_x, y=150, anchor="center")

word_label = tk.Label(screen, text="Word", font=LABEL_FONT_WORD, bg="White")
word_label.place(x=text_x, y=263, anchor="center")


screen.mainloop()
