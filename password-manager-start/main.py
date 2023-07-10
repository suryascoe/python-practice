from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_name.get()
    try:
        with open("data.json", "r") as data:
            jdata = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in jdata:
            email = jdata[website]['email']
            password = jdata[website]['password']
            messagebox.showinfo(title=website,
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_name.get()
    email = email_username_name.get()
    password_entry = password_text.get()
    new_data = {website: {"email": email, "password": password_entry}}

    if len(website) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                jdata = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            jdata.update(new_data)
            with open("data.json", "w") as data:
                json.dump(jdata, data, indent=4)
        finally:
            website_name.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

# Website Label
web_lbl = Label(text="Website:")
web_lbl.grid(column=0, row=1)

# Email/Username Label
email_username_lbl = Label(text="Email/Username:")
email_username_lbl.grid(column=0, row=2)

# Email/Username Label
password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

# Entry Website Name
website_name = Entry(width=33)
website_name.grid(column=1, row=1)
website_name.focus()

# Entry Email/Username Name
email_username_name = Entry(width=51)
email_username_name.grid(column=1, row=2, columnspan=2)
email_username_name.insert(0, "surya@gmail.com")

# Entry Email/Username Name
password_text = Entry(width=33)
password_text.grid(column=1, row=3)

# Generate Password Button
generate_password_btn = Button(text="Generate Password", command=generate_password, width=14)
generate_password_btn.grid(column=2, row=3)

# Add Button
add_btn = Button(text="Add", width=44, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

# Search Button
search_btn = Button(text="Search", command=find_password, width=14)
search_btn.grid(column=2, row=1)

window.mainloop()
