from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# --------------------------------- PASSWORD GENERATOR -----------------------#
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)  # Clear the entry field before inserting
    password_input.insert(0, password)
    pyperclip.copy(password)  # Copy the password to clipboard


# ---------------------------------- SAVE PASSWORD -----------------------#
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {website: {"Username": username, "Password": password}}

    if not website or not username or not password:
        messagebox.showerror(title="Error", message="Please enter all details.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)  # Reading existing data
    except (FileNotFoundError, json.JSONDecodeError):  # Handle missing or corrupted file
        data = {}

    data.update(new_data)  # Update with new data

    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)  # Save updated data
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Could not save data: {e}")
        return

    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
try:
    logo = PhotoImage(file="logo.png")
    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=logo)
    canvas.grid(row=0, column=1, columnspan=2)
except:
    messagebox.showwarning("Warning", "Logo image not found. Proceeding without logo.")

# Labels and Entry Fields
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="w")

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky="w")
username_input.insert(0, "mohammedarmaand@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="w")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()