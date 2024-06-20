"""Module to create and update a scoreboard"""

from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Scoreboard creation."""

    def __init__(self) -> None:
        super().__init__()
        self.count = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("gray")
        self.speed("fastest")
        self.goto(x=0, y=256)
        self.update_scoreboard()

    def update_scoreboard(self):
        """The string generation for scoreboard."""
        self.clear()
        self.write(
            arg=f"Score: {self.count} - High Score: {self.high_score}",
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        """Clear the turtle and update the count."""
        self.count += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        """New reset method that checks for high-score."""

        if self.count > self.high_score:
            self.high_score = self.count
        self.count = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """
    #     Print out game over.
    #     """
    #     self.goto(0, 0)
    #     self.write(
    #         arg="GAME OVER",
    #         align=ALIGN,
    #         font=FONT,
    #     )
