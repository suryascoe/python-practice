from tkinter import *


def button_clicked():
    if not user_input.get():
        my_label.config(text="Button got Clicked")
    else:
        my_label.config(text=user_input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button1 = Button(text="New Button")
button1.grid(column=2, row=0)

# Entry
user_input = Entry(width=30)
user_input.grid(column=3, row=2)

window.mainloop()
