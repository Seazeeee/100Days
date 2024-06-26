"""Module that creates the ball."""

from turtle import Turtle
from scoreboard import Scoreboard

SCOREBOARD = Scoreboard()


class Ball(Turtle):
    """A class that creates and moves the ball."""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed_num = 0.1

    def move(self):
        """
        Creates a while loop that moves the ball to the top right corner.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Wall Bounce."""
        self.y_move *= -1

    def paddle_bounce(self):
        """Paddle Bounce."""

        self.x_move *= -1
        self.speed_num *= 0.9

    def paddle_miss(self):
        """Detects if the balls passes the paddle"""

        if self.xcor() >= 380:
            self.goto(0, 0)
            self.paddle_bounce()
            SCOREBOARD.l_point()
            self.speed_num = 0.1
        elif self.xcor() <= -380:
            self.goto(0, 0)
            self.paddle_bounce()
            SCOREBOARD.r_point()
            self.speed_num = 0.1
