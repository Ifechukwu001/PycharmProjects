from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("PONG")
screen.setup(width=1080, height=620)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-520, 0))
r_paddle = Paddle((510, 0))
ball = Ball()
score_board = ScoreBoard()

game_is_on = True


# def end_game():
#     global game_is_on
#     game_is_on = False


screen.listen()
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
screen.onkey(fun=r_paddle.move_up, key="o")
screen.onkey(fun=r_paddle.move_down, key="l")
# screen.onkey(fun=end_game, key="Space")

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect wall collision.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if (ball.distance(l_paddle) < 50 and -510 < ball.xcor() < -495) or (ball.distance(r_paddle) < 50
                                                                        and 500 > ball.xcor() > 480):
        ball.bounce_x()

    # Detect when l_paddle misses.
    if ball.xcor() < -540:
        ball.refresh()
        score_board.r_point()

    # Detect when r_paddle misses.
    if ball.xcor() > 540:
        ball.refresh()
        score_board.l_point()

screen.exitonclick()
