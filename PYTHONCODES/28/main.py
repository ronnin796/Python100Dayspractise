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
reps = 3
timer_countdown = None
BASE_DIR = Path(__file__).parent
START_TEXT = "00:00"

# ---------------------------- TIMER RESET ------------------------------- #


def restart():
    global reps
    screen.after_cancel(timer_countdown)
    canvas.itemconfig(countdown_text, text=START_TEXT)
    check_label.config(text="")
    timer_label.config(text="Timer")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    SEC = 60
    if reps % 2 != 0:
        timer_label.config(text="Work Time")
        countdown(WORK_MIN * SEC)
    elif reps % 8 == 0:
        timer_label.config(text="Long Break Time", fg=RED)
        countdown(LONG_BREAK_MIN * SEC)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break Time", fg=PINK)
        countdown(SHORT_BREAK_MIN * SEC)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(timer):
    minutes = timer // 60
    seconds = timer % 60
    global timer_countdown
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    if timer >= 0:
        canvas.itemconfig(countdown_text, text=f"{minutes}:{seconds}")
        timer_countdown = screen.after(1000, countdown, timer - 1)
    else:
        check_marks = "✓" * (reps // 2)
        check_label.config(text=check_marks)
        start()


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
    100, 130, text=START_TEXT, fill="white", font=(FONT_NAME, 35, "bold")
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
    screen, text="", fg="Green", bg=YELLOW, font=("Arial", 20, "bold")
)
check_label.grid(row=3, column=1)
screen.mainloop()
