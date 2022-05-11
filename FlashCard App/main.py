from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")


def remove_card():
    data_dict.remove(word)
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


def flip(e_word):
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=e_word, fill="white")
    canvas.itemconfig(card_img, image=card_back_img)


def generate_word():
    global word
    word = random.choice(data_dict)
    french_word = word["French"]
    english_word = word["English"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_img, image=card_front_img)

    root.after(3000, flip, english_word)


root = Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 130, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 260, text="", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=generate_word)
wrong_button.grid(row=2, column=0)

right_button = Button(image=right_img, highlightthickness=0, border=0, command=remove_card)
right_button.grid(row=2, column=1)


generate_word()





root.mainloop()