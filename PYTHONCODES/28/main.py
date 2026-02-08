from tkinter import font
import tkinter as tk
from pathlib import Path
import time

screen = tk.Tk()
my_font = font.Font(family="Arial", size=35, weight="bold", slant="roman")
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


def restart():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    # canvas.itemconfig(countdown_text, text="5")
    countdown(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(timer):
    minutes = timer // 60
    seconds = timer % 60
    if timer >= 0:
        canvas.itemconfig(countdown_text, text=f"{minutes}:{seconds}")
        screen.after(1000, countdown, timer - 1)


# ---------------------------- UI SETUP ------------------------------- #

screen.title("Timer")
screen.config(padx=100, pady=50, bg=YELLOW)
timer_label = tk.Label(
    screen, text="Timer", fg="Green", bg=YELLOW, font=("Arial", 20, "bold")
)
timer_label.grid(row=0, column=1)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
toamto_image = BASE_DIR / "./tomato.png"
tomato = tk.PhotoImage(file=toamto_image)
canvas.create_image(100, 112, image=tomato)
canvas.grid(row=1, column=1)
countdown_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
button_start = tk.Button(
    screen, text="start", font=("Arial", 16, "bold"), command=start
)
button_start.grid(row=2, column=0, pady=20)

button_reset = tk.Button(
    screen, text="reset", font=("Arial", 16, "bold"), command=restart
)
button_reset.grid(row=2, column=2, pady=20)

check_label = tk.Label(
    screen, text="✓", fg="Green", bg=YELLOW, font=("Arial", 20, "bold")
)
check_label.grid(row=3, column=1)
screen.mainloop()
