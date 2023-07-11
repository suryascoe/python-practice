from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# Reading Data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=current_card["French"], fill="black")
    flash_card.itemconfig(canvas_image, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=current_card["English"], fill="white")
    flash_card.itemconfig(canvas_image, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Import Image
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Canvas
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(column=0, row=0, columnspan=2)
canvas_image = flash_card.create_image(400, 270, image=card_front_img)
card_title = flash_card.create_text(400, 150, font=("Arial", 40, "italic"), text="")
card_word = flash_card.create_text(400, 263, font=("Ariel", 60, "bold"), text="")

# Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()
