from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def up(self):
        """Moves the turtle up by 10 pixels"""
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def win(self):
        if self.ycor() == FINISH_LINE_Y:
            self.reset()
            # Increase scoreboard | Increase car speed