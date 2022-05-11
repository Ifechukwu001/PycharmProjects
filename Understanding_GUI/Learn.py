import random
import turtle as t
from random import choice

timmy =t.Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# for method in range(4):
#     timmy.forward(200)
#     timmy.rt(90)

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     x, y = timmy.pos()  # Get the position of the turtle in a tuple.
#     timmy.goto((x + 5), y)  # Move the coordinate of the turtle to the new position.
#     timmy.pendown()


# def draw_shape(side_of_shape):
#     for _ in range(side_of_shape):
#         timmy.forward(50)
#         timmy.right((360 / side_of_shape))
#
#
# shape_side = 3
# while shape_side < 13:
#     colors = ["gainsboro", "cornflowerblue", "darkblue", "cyan", "green", "yellow", "sandybrown", "darkred",
#               "deeppink", "lavender"]
#
#     color = choice(colors)
#     timmy.color(color)
#     draw_shape(shape_side)
#     shape_side += 1

t.colormode(255)
timmy.speed("fastest")
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color
#
#
# direction = [0, 90, 180, 270]
# angle = choice(direction)
# size = 5
# speed = 1
# lenght = 20
# while True:
#     angle = choice(direction)
#     color = random_color()
#     timmy.color(color)
#     timmy.pen(pensize=size, speed=speed)
#     timmy.forward(lenght)
#     timmy.setheading(angle)
#     speed += 0.5
#     size += 0.05
#     lenght += 0.1


def sprirato(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


sprirato(2)

screen = t.Screen()
screen.exitonclick()