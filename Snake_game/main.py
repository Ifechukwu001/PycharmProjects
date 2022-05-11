from turtle import Screen
from snake import Snake
from food import Food
from poison import Poison
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
poison = Poison()
poison2 = Poison()
poison3 = Poison()
poison4 = Poison()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.13)

    # Detect if only the head is remaining.
    if len(snake.segments) == 1 or score_board.score == -1:
        score_board.restart()
        snake.restart()

    # Detect collision with food.
    if snake.head.distance(food) < 16:
        food.refresh()
        poison.refresh()
        poison2.refresh()
        poison3.refresh()
        poison4.refresh()
        snake.extend()
        score_board.add_score()
        score_board.refresh()

    # Detect collision with poison.
    if snake.head.distance(poison) < 16 or snake.head.distance(poison2) < 16 or snake.head.distance(poison3) < 16 or \
            snake.head.distance(poison4) < 16:
        food.refresh()
        poison.refresh()
        poison2.refresh()
        poison3.refresh()
        poison4.refresh()
        snake.reduce()
        score_board.remove_score()
        score_board.refresh()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.restart()
        snake.restart()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.restart()
            snake.restart()

    # Make the snake move.
    snake.move()


screen.exitonclick()
