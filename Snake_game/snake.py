from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_CONSTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reduce(self):
        removed_segment = self.segments.pop(-1)
        removed_segment.hideturtle()

    def restart(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_CONSTANT)

    def move_up(self):
        curr_direction = self.segments[0].heading()
        if curr_direction == 0 or curr_direction == 180:
            self.head.setheading(UP)

    def move_down(self):
        curr_direction = self.segments[0].heading()
        if curr_direction == 0 or curr_direction == 180:
            self.head.setheading(DOWN)

    def move_left(self):
        curr_direction = self.segments[0].heading()
        if curr_direction == 90 or curr_direction == 270:
            self.head.setheading(LEFT)

    def move_right(self):
        curr_direction = self.segments[0].heading()
        if curr_direction == 90 or curr_direction == 270:
            self.head.setheading(RIGHT)