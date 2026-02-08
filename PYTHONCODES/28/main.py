from tkinter import font
import tkinter as tk
from pathlib import Path

screen = tk.Tk()
my_font = font.Font(family="Arial", size=35, weight="bold", slant="italic")
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


BASE_DIR = Path(__file__).parent
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

screen.title("Timer")
screen.config(padx=100, pady=100, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
toamto_image = BASE_DIR / "./tomato.png"
tomato = tk.PhotoImage(file=toamto_image)
canvas.create_image(100, 112, image=tomato)
canvas.pack()
canvas.create_text(100, 130, text="00:00", fill="White", font=my_font)
screen.mainloop()
