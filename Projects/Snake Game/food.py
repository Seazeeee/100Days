"""Module that creates food for snake game"""
from turtle import Turtle
import random


class Food(Turtle):
    """Create a food for the snake to eat."""
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.50, stretch_wid=0.50)
        self.color("aqua")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x + .5, random_y + .5)
        self.refresh()

    def refresh(self):
        """Refresh the food so that it goes to a new location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
