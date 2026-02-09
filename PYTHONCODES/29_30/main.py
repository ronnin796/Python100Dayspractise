import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from random import shuffle, randint, choice
import pyperclip
import json

# ---------------------------- FONT SETUP ------------------------------- #
TITLE_FONT = ("Arial", 24, "bold")
LABEL_FONT = ("Arial", 14, "normal")
ENTRY_FONT = ("Arial", 14, "normal")
BUTTON_FONT = ("Arial", 13, "bold")

BASE_DIR = Path(__file__).parent
screen = tk.Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20, bg="White")


# ---------------------------- SEARCH ------------------------------- #
def search_password(website_key):
    try:
        with open(BASE_DIR / "data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS", message="No passwords registered.")
    else:
        try:
            website_entry = data[website_key]
        except KeyError:
            messagebox.showinfo(
                title="OOPS",
                message="No entry for this website . Please make sure the spelling is correct!",
            )
        else:
            password = website_entry["password"]
            email = website_entry["email"]
            messagebox.showinfo(
                title=website_key,
                message=f"Email = {email} , Password = {password}",
            )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
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
    new_dictionary = {website: {"email": email, "password": password}}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="OOPS", message="Please make sure no fields are empty."
        )
    else:
        try:
            with open(BASE_DIR / "data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_dictionary)

        except FileNotFoundError:
            with open(BASE_DIR / "data.json", mode="w") as file:
                json.dump(new_dictionary, file, indent=4)

        else:
            with open(BASE_DIR / "data.json", mode="w") as file:
                json.dump(data, file, indent=4)

    reset()


def reset():
    website_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
canvas = tk.Canvas(width=400, height=662, bg="White", highlightthickness=0)
guard_image = BASE_DIR / "frieren.png"

app_label = tk.Label(
    screen,
    text="Frieren the Password Keeper",
    fg="Green",
    bg="White",
    font=TITLE_FONT,
)
app_label.grid(row=0, column=1, pady=(0, 10))

saitama = tk.PhotoImage(file=guard_image)
canvas.create_image(180, 331, image=saitama)
canvas.grid(row=1, column=1)

# Website input
website_label = tk.Label(
    screen,
    text="Website:",
    fg="Green",
    bg="White",
    font=LABEL_FONT,
)
website_label.grid(row=2, column=0, pady=5, sticky="e")

website_input = tk.Entry(screen, font=ENTRY_FONT, width=45)
website_input.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")
website_input.focus()
# Search Button
search_button = tk.Button(
    screen,
    text="Search",
    font=BUTTON_FONT,
    command=lambda: (search_password(website_input.get())),
)
search_button.grid(row=2, column=2, sticky="e")
# Email / Username
email_label = tk.Label(
    screen,
    text="Email:",
    fg="Green",
    bg="White",
    font=LABEL_FONT,
)
email_label.grid(row=3, column=0, pady=5, sticky="e")

email_input = tk.Entry(screen, font=ENTRY_FONT, width=55)
email_input.grid(row=3, column=1, columnspan=2, pady=5)
email_input.insert(0, "nischalchy15@gmail.com")
# Password section
password_label = tk.Label(
    screen,
    text="Password:",
    fg="Green",
    bg="White",
    font=LABEL_FONT,
)
password_label.grid(row=4, column=0, pady=5, sticky="e")

password_input = tk.Entry(screen, font=ENTRY_FONT, width=43)
password_input.grid(row=4, column=1, sticky="w")

generate_button = tk.Button(
    screen, text="Generate", font=BUTTON_FONT, command=generate_password
)
generate_button.grid(row=4, column=2, sticky="w")

# Add Button
add_button = tk.Button(
    screen,
    text="Add",
    font=BUTTON_FONT,
    command=save_password,
    width=53,
)
add_button.grid(row=5, column=1, pady=10, columnspan=2)

screen.mainloop()
