"""A Module that creates a Pong Game."""

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


# Creating the SCreen.
SCREEN = Screen()
SCREEN.bgcolor("black")
SCREEN.title("Ponging")
SCREEN.setup(width=800, height=600)
SCREEN.tracer(0)

# Create necessary variables.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
game_is_on = True

SCREEN.listen()  # Declare the listener

# Creating the 4 different movement keys
SCREEN.onkey(r_paddle.up, "Up")  # IMPORTANT: Dont use ()
SCREEN.onkey(r_paddle.down, "Down")
SCREEN.onkey(l_paddle.up, "w")
SCREEN.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(ball.speed_num)  # slow the game down
    SCREEN.update()
    ball.move()
    ball.paddle_miss()

    # Collision Detection with Wall

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    # Detect collision with r_paddle

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.paddle_bounce()

SCREEN.exitonclick()
