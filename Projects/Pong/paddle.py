"""Module that creates the paddle."""

from turtle import Turtle


class Paddle(Turtle):
    """Class that creates paddles"""

    def __init__(self, cords) -> None:
        super().__init__()
        self.goto(x=cords[0], y=cords[-1])
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.color("white")

    def up(self):
        """Moves it up 20 units"""
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        """Moves it down 20 units"""
        self.goto(self.xcor(), self.ycor() - 20)
