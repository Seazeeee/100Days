"""Module that writes the state on the screen."""

import pandas as df
from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 10, "normal")
DATA = df.read_csv("Projects/US States Game/50_states.csv")


class WriteStates(Turtle):
    """Class that inherits from Turtle and writes the states name
    on the scree."""

    def __init__(self, answer) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.answer = answer
        self.produce_text()

    def produce_text(self):
        """Method to produce text and grab x, y values."""

        x = DATA[DATA.state == str(self.answer).title()].x.values[0]
        y = DATA[DATA.state == str(self.answer).title()].y.values[0]

        self.goto(
            x=x,
            y=y,
        )

        self.write(
            arg=f"{self.answer.title()}",
            align=ALIGN,
            font=FONT,
        )

    def check_new(self, new_answer: str):
        check_answer = DATA["state"][
            DATA.state.str.lower() == str(new_answer).lower()
        ].any()

        return check_answer
