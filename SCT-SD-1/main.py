import tkinter as tk
from tkinter import messagebox

def update_entry(entry, value):
    entry.delete(0, tk.END)
    entry.insert(0, value)

def converter():
    celsius = celsius_input.get()
    fahrenheit = fahrenheit_input.get()
    kelvin = kelvin_input.get()

    try:
        if celsius:
            celsius = float(celsius)
            fahrenheit = round((9/5) * celsius + 32, 2)
            kelvin = round(celsius + 273.15, 2)

            update_entry(fahrenheit_input, fahrenheit)
            update_entry(kelvin_input, kelvin)

        elif fahrenheit:
            fahrenheit = float(fahrenheit)
            celsius = round((fahrenheit - 32) * 5/9, 2)
            kelvin = round(celsius + 273.15, 2)

            update_entry(celsius_input, celsius)
            update_entry(kelvin_input, kelvin)

        elif kelvin:
            kelvin = float(kelvin)
            celsius = round(kelvin - 273.15, 2)
            fahrenheit = round((9/5) * celsius + 32, 2)

            update_entry(celsius_input, celsius)
            update_entry(fahrenheit_input, fahrenheit)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
    
def reset():
    celsius_input.delete(0, tk.END)
    fahrenheit_input.delete(0, tk.END)
    kelvin_input.delete(0, tk.END)
    celsius_input.focus()

# UI
window = tk.Tk()
window.title("Temperature Converter!")
window.config(padx=40, pady=40)

title = tk.Label(text="Temperature Converter", font=("Arial", 16, "bold"))
title.grid(column=0, row=0, columnspan=2, pady=10)

celsius_label = tk.Label(text="Celsius (°C)", font=("Arial", 11))
celsius_label.grid(column=0, row=1, pady=5)

celsius_input = tk.Entry(width=15, justify="center")
celsius_input.grid(column=1, row=1)

fahrenheit_label = tk.Label(text="Fahrenheit (°F)", font=("Arial", 11))
fahrenheit_label.grid(column=0, row=2, pady=5)

fahrenheit_input = tk.Entry(width=15, justify="center")
fahrenheit_input.grid(column=1, row=2)

kelvin_label = tk.Label(text="Kelvin (K)", font=("Arial", 11))
kelvin_label.grid(column=0, row=3, pady=5)

kelvin_input = tk.Entry(width=15, justify="center")
kelvin_input.grid(column=1, row=3)

converter_button = tk.Button(text="Convert", width=12, bg="#4CAF50", fg="white", command=converter)
converter_button.grid(column=0, row=4, pady=15)

reset_button = tk.Button(text="Clear", width=12, bg="#f44336", fg="white", command=reset)
reset_button.grid(column=1, row=4)

window.bind("<Return>", lambda event: converter())
celsius_input.focus()

window.mainloop()