from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fwd():
    tim.forward(10)


def move_bk():
    tim.backward(10)


def bend_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def bend_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_fwd, key="w")
screen.onkey(fun=move_bk, key="s")
screen.onkey(fun=bend_left, key="a")
screen.onkey(fun=bend_right, key="d")
screen.onkey(fun=clean, key="c")





screen.exitonclick()