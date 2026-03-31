from tkinter import *
from tkinter import ttk, messagebox
import random

BACKGROUND = "#1e1e2f"
FOREGROUND = "#ffffff"

number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 7

def set_difficulty(event=None):
    global number_to_guess, attempts, max_attempts

    level = select_level.get()

    if level == "Easy":
        max_attempts = 10
    elif level == "Medium":
        max_attempts = 7
    else:
        max_attempts = 5

    number_to_guess = random.randint(1, 100)
    attempts = 0

    result_label.config(text=f"You have {max_attempts} attempts. Guess between 1–100", fg=FOREGROUND)

    guess_entry.delete(0, END)
    guess_entry.config(state="normal")
    guess_button.config(state="normal")

def check_guess():
    global attempts

    user_input = guess_entry.get().strip()

    if user_input == "":
        messagebox.showwarning("Input Error", "Please enter a number!")
        return
    
    if not user_input.isdigit():
        messagebox.showerror("Invalid Input", "Only numbers are allowed!")
        guess_entry.delete(0, END)
        return
    
    guess = int(user_input)

    if guess < 1 or guess > 100:
        messagebox.showwarning("Out of Range", "Enter a number between 1 and 100")
        guess_entry.delete(0, END)
        return
    
    attempts += 1
    remaining = max_attempts - attempts
    
    if guess > number_to_guess:
        result_label.config(text= f"📉 Too High! Remaining: {remaining}", fg="#ff6b6b")

    elif guess < number_to_guess:
        result_label.config(text= f"📈 Too Low! Remaining: {remaining}", fg="#f7b801")

    else:
        result_label.config(text= f"🎉 Correct! You won in {attempts} attempts!", fg="#06d6a0")
        messagebox.showinfo("🎉 Congratulations!", "You guessed the number!")
        end_game()
        return
    
    if attempts >= max_attempts:
        result_label.config(text=f"💀 Game Over! Number was {number_to_guess}", fg="red")
        messagebox.showinfo("Game Over", f"The number was {number_to_guess}")
        end_game()

    guess_entry.delete(0, END)

def end_game():
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

def reset_game():
    global number_to_guess, attempts

    number_to_guess = random.randint(1, 100)
    attempts = 0

    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    guess_entry.delete(0, END)

    result_label.config(text=f"Game Reset! You have {max_attempts} attempts.", fg=FOREGROUND)

# UI
window = Tk()
window.title("🎯 Number Guessing Game")
window.config(padx=40, pady=40, bg=BACKGROUND)

title = Label(text="🎯 Number Guessing Game", font=("Arial", 22, "bold"), bg=BACKGROUND, fg=FOREGROUND)
title.grid(row=0, column=0, columnspan=2, pady=10)

subtitle = Label(text="Select Difficulty Level", font=("Arial", 14), bg=BACKGROUND, fg=FOREGROUND)
subtitle.grid(row=1, column=0, columnspan=2, pady=10)

select_level = ttk.Combobox(window, values=["Easy", "Medium", "Hard"], state="readonly", width=15)
select_level.set("Medium")
select_level.grid(row=2, column=0, columnspan=2, pady=10)
select_level.bind("<<ComboboxSelected>>", set_difficulty)

guess_entry = Entry(width=12, font=("Arial", 14), justify=CENTER)
guess_entry.grid(row=3, column=0, pady=10)

guess_button = Button(text="Check Guess", bg="#4cc9f0", fg="black", font=("Arial", 12, "bold"), padx=10, command=check_guess)
guess_button.grid(row=3, column=1, pady=10)

result_label = Label(text="You have 7 attempts. Guess between 1–100", font=("Arial", 14), bg=BACKGROUND, fg=FOREGROUND)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

reset_button = Button(text="🔄 Restart Game", bg="#ff9f1c", fg="black", font=("Arial", 12, "bold"), padx=10, command=reset_game)
reset_button.grid(row=5, column=0, columnspan=2, pady=10)

window.bind("<Return>", lambda event: check_guess())
guess_entry.focus()

window.mainloop()