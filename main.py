from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn ={}
try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    or_data = pandas.read_csv("data/french_words.csv")
    to_learn = or_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

current_card = {}


def guess():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip)


def know():
    to_learn.remove(current_card)
    n_data = pandas.DataFrame(to_learn)
    n_data.to_csv("data/words_to_learn.csv", index=False)
    guess()


def flip():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')


window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
flip_timer = window.after(3000, flip)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=know)
right.grid(column=0, row=1)
wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=guess)
wrong.grid(column=1, row=1)
guess()
window.mainloop()
