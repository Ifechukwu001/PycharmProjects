from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)

user_input = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour")

colors = ["red", "yellow", "orange", "green", "blue", "purple"]
y_position = [-90, -50, -10, 30, 70, 110]
all_turtles = []
is_game_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:

        if turtle.xcor() > 240:
            is_game_on = False
            winning_turtle = turtle.pencolor().capitalize()
            if winning_turtle.lower() == user_input:
                print(f"You win! {winning_turtle} is the winner.")
            else:
                print(f"You lose! {winning_turtle} is the winner.")
            continue
        new_position = randint(0, 10)
        turtle.forward(new_position)

screen.exitonclick()