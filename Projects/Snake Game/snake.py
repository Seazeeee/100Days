"""Module that creates the snakes for the snake game."""

from turtle import Turtle


CORDS = [(0, 0), (-20, 0), (-40, 0)]  # Declaring CORDS variable.
MOVE_DISTANCE = 20


class Snake:
    """Creates Snakes alongside making them move"""
    def __init__(self):
        self.dict_turtles = {}
        self.create_snake()

    def create_snake(self):
        """
        Generates the starting snake
        """
        self.index = 0

        for num_index in CORDS:
            # Create the different turtle methods needed; adds them to a dict.
            self.dict_turtles[self.index] = Turtle(shape="square")
            self.dict_turtles[self.index].penup()
            self.dict_turtles[self.index].color("white")
            self.dict_turtles[self.index].goto(num_index)
            self.index += 1

    def move(self):
        """
        Allows the previous segment to move to the one in front of it
        """
        for num_turtle in range(len(self.dict_turtles) - 1, 0, -1):
            # Grab the front turtle and its cords.
            forward_turtle = self.dict_turtles[num_turtle - 1]
            new_x = forward_turtle.xcor()
            new_y = forward_turtle.ycor()
            # Move the turtle behind to the new cords.
            self.dict_turtles[num_turtle].goto(x=new_x, y=new_y)
        self.dict_turtles[0].forward(MOVE_DISTANCE)
