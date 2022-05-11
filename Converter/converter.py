from tkinter import *


def convertion(number):
    return round(number * 1.609)


def onclick():
    feild = float(user_input.get())
    result = convertion(feild)
    result_label.config(text=f"{result}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=50)
window.config(padx=20, pady=10)

user_input = Entry(width=10)
user_input.grid(row=0, column=1)

u_label = Label(text="Miles")
u_label.grid(row=0, column=2)

compare_label = Label(text="is equal to")
compare_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

r_label = Label(text="Km")
r_label.grid(row=1, column=2)

button = Button(text="Convert", command=onclick)
button.grid(row=2, column=1)

window.mainloop()
