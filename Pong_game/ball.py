from turtle import Turtle

SCREEN_HEIGHT = 300


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_increment = 10
        self.y_increment = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_increment *= -1

    def bounce_x(self):
        self.x_increment *= -1
        self.move_speed -= 0.01

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05