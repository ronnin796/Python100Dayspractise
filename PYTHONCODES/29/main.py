from tkinter import font
import tkinter as tk
from pathlib import Path
import time
from random import shuffle, randint, choice
import pyperclip

FONT = ("Arial", 20, "bold")
BASE_DIR = Path(__file__).parent
screen = tk.Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20, bg="White")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0, tk.END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    with open(BASE_DIR / "./data.txt", mode="a") as file:
        password_data = f"{website} | {email} | {password} \n"
        file.write(password_data)
        file.close()
    reset()


def reset():
    website_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #


canvas = tk.Canvas(width=400, height=662, bg="White", highlightthickness=0)
guard_image = BASE_DIR / "./frieren.png"
app_label = tk.Label(
    screen,
    text="Frieren the Password Keeper",
    fg="Green",
    bg="White",
    font=FONT,
)
app_label.grid(row=0, column=1)
saitama = tk.PhotoImage(file=guard_image)
canvas.create_image(180, 331, image=saitama)
canvas.grid(row=1, column=1)

# Website input
website_label = tk.Label(
    screen,
    text="Website:",
    fg="Green",
    bg="White",
    font=FONT,
)
website_label.grid(row=2, column=0)
website_input = tk.Entry(screen, font=FONT, width=36)
# website_input.insert(0, "Enter the Website")
website_input.grid(row=2, column=1, columnspan=2, sticky="w")
website_input.focus()

# Email /Username Section

email_label = tk.Label(
    screen,
    text="Email:",
    fg="Green",
    bg="White",
    font=FONT,
)
email_label.grid(row=3, column=0)
email_input = tk.Entry(screen, font=FONT, width=36)
# email_input.insert(0, "Enter the email")
email_input.grid(row=3, column=1, columnspan=2, sticky="w")

# Generate Password Section

password_label = tk.Label(
    screen,
    text="Password:",
    fg="Green",
    bg="White",
    font=FONT,
)
password_label.grid(row=4, column=0)
password_input = tk.Entry(screen, font=FONT, width=21)
# password_input.insert(0, "Enter the password")
password_input.grid(row=4, column=1, columnspan=2, sticky="w")

generate_button = tk.Button(
    screen, text="Generate", font=FONT, command=generate_password
)
generate_button.grid(row=4, column=2)

# Add Button
add_button = tk.Button(screen, text="Add", font=FONT, command=save_password, width=35)
add_button.grid(row=5, column=1, columnspan=2, sticky="w")

screen.mainloop()
