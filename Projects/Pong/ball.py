"""Module that creates the ball."""

from turtle import Turtle


class Ball(Turtle):
    """A class that creates and moves the ball."""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move()

    def move(self):
        """
        Creates a while loop that moves the ball to the top right corner.
        """

        self.goto(self.xcor() + 10, self.ycor() + 10)

