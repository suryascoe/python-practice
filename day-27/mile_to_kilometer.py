from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(pady=5, padx=5)


def miletokilometer():
    km = user_input.get()
    if km != "":
        km = round(float(km) * 1.689)
        output_lbl.config(text=f"{km}")
    else:
        output_lbl.config(text=0)


# Button Calculate
cal_button = Button(text="Calculate", command=miletokilometer)
cal_button.grid(column=1, row=2)

# Entry of User Input
user_input = Entry(width=20)
user_input.grid(column=1, row=0)

# Labels ...
# 1. Mile Label
mile_lbl = Label()
mile_lbl.config(text="Miles")
mile_lbl.grid(column=2, row=0)

# 2. Is equal Label
eq_lbl = Label()
eq_lbl.config(text="is equal to")
eq_lbl.grid(column=0, row=1)

# 3. Kilometer label
km_lbl = Label()
km_lbl.config(text="Km")
km_lbl.grid(column=2, row=1)

# 4. Output Label
output_lbl = Label()
output_lbl.config(text=0)
output_lbl.grid(column=1, row=1)

window.mainloop()
