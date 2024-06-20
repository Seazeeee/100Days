"""Module that creates the snakes for the snake game."""

from turtle import Turtle

# Creating CONSTANTS
CORDS = [(0, 0), (-20, 0), (-40, 0)]  # Declaring CORDS variable.
MOVE_DISTANCE = 20  # Move variable for testing.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creates Snakes alongside making them move"""
    def __init__(self):
        self.dict_turtles = []
        self.create_snake()
        self.head = self.dict_turtles[0]

    def create_snake(self):
        """
        Generates the starting snake
        """
        for position in CORDS:
            # Create the different turtle methods needed; adds them to a dict.
            self.add_segment(position)

    def add_segment(self, position):
        """Creates the segments for the snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.dict_turtles.append(new_segment)

    def extend(self):
        """Extends the snake."""
        self.add_segment(self.dict_turtles[-1].position())

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets heading to 90 degrees; Checks heading to verify it can."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets heading to 270 degrees; Checks heading to verify it can."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets heading to 180 degrees; Checks heading to verify it can."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets heading to 0 degrees; Checks heading to verify it can."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """Resets the snake completely."""
        for seg in self.dict_turtles:
            seg.goto(1000, 1000)
        self.dict_turtles.clear()
        self.create_snake()
        self.head = self.dict_turtles[0]
