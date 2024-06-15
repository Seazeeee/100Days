"""Module that creates the ball."""

from turtle import Turtle


class Ball(Turtle):
    """A class that creates and moves the ball."""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """
        Creates a while loop that moves the ball to the top right corner.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):

        self.y_move *= -1
