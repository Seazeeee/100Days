"""Module that creates the scoreboard."""

from turtle import Turtle


class Scoreboard(Turtle):
    """A turtle class that displays the score."""

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 60, "normal"))

    def l_point(self):
        """Adds a point to the left side."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Adds a point to the right side."""
        self.r_score += 1
        self.update_scoreboard()
