"""Module that creates the paddle."""

from turtle import Turtle


class Paddle(Turtle):
    """Class that creates paddles"""

    def __init__(self, cords) -> None:
        super().__init__()
        self.goto(x=cords[0], y=cords[-1])
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.color("white")

    def up(self):
        """Moves it up 20 units"""
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        """Moves it down 20 units"""
        self.goto(self.xcor(), self.ycor() - 20)
