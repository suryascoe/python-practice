from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lbl.config(text="Timer")
    check_lbl.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    if reps % 8 == 0:
        title_lbl.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_lbl.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_lbl.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_text = "✔️" * math.floor(reps / 2)
            check_lbl.config(text=f"{check_text}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label Timer
title_lbl = Label()
title_lbl.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_lbl.grid(column=1, row=0)

# Button Start
start_btn = Button()
start_btn.config(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

# Button Reset
reset_btn = Button()
reset_btn.config(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

# Check Text
check_lbl = Label()
check_lbl.config(fg=GREEN, bg=YELLOW)
check_lbl.grid(column=1, row=3)

window.mainloop()
