"""Module that creates the paddle."""

from turtle import Turtle


class Paddle(Turtle):
    """Class that creates paddles"""

    def __init__(self) -> None:
        super().__init__()
        self.goto(x=350, y=0)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")

    def up(self):
        """Moves it up 20 units"""
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        """Moves it down 20 units"""
        self.goto(self.xcor(), self.ycor() - 20)
