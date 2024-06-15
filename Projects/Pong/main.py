"""A Module that creates a Pong Game."""

from turtle import Screen
from paddle import Paddle

# Creating the SCreen.
SCREEN = Screen()
SCREEN.bgcolor("black")
SCREEN.title("Ponging")
SCREEN.setup(width=800, height=600)
SCREEN.tracer(0)

# Create necessary variables.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_is_on = True

SCREEN.listen()  # Declare the listener

# Creating the 4 different movement keys
SCREEN.onkey(r_paddle.up, "Up")  # IMPORTANT: Dont use ()
SCREEN.onkey(r_paddle.down, "Down")
SCREEN.onkey(l_paddle.up, "w")
SCREEN.onkey(l_paddle.down, "s")

while game_is_on:
    SCREEN.update()


SCREEN.exitonclick()
