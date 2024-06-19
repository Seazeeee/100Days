"""Module that creates and handles teh scoreboard."""
from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Scoreboard creation."""

    def __init__(self) -> None:
        super().__init__()
        self.count = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(x=-256, y=256)
        self.update_scoreboard()

    def update_scoreboard(self):
        """The string generation for scoreboard."""
        self.write(
            arg=f"Level: {self.count}",
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        """Clear the turtle and update the count."""
        self.count += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """
        Print out game over.
        """
        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            align=ALIGN,
            font=FONT,
        )