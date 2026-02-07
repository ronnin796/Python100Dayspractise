import tkinter as tk


window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def convert():
    """Convert Celsius to Fahrenheit and update the label."""
    try:
        celsius = float(entry_input.get())
        fahrenheit = (9 / 5) * celsius + 32
        fahrenheit_label.config(text=f"{fahrenheit:.1f} °F")
    except ValueError:
        fahrenheit_label.config(text="Please enter a valid number!")


prompt_label = tk.Label(
    window, text="Enter temperature in Celsius:", font=("Arial", 20, "bold")
)
prompt_label.grid(row=0, column=1, columnspan=2, pady=(0, 20))

celcius_label = tk.Label(window, text="°C", font=("Arial", 20, "bold"))
celcius_label.grid(row=1, column=2, sticky="w")

fahrenheit_label = tk.Label(window, text="°F", font=("Arial", 20, "bold"))
fahrenheit_label.grid(row=3, column=1, columnspan=2, pady=(20, 0))


entry_input = tk.Entry(window, font=("Arial", 16))
entry_input.insert(0, "0")
entry_input.grid(row=1, column=1, padx=(0, 10))


button = tk.Button(window, text="Convert", font=("Arial", 16, "bold"), command=convert)
button.grid(row=2, column=1, columnspan=2, pady=20)


window.mainloop()
