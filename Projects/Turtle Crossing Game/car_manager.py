"""Module that creates and manages the cars."""
import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Creates and manages the cars."""

    def __init__(self) -> None:
        super().__init__()
        self.cars_list: list[Turtle] = []
        self.create_all_cars()
        self.hideturtle()
        self.movement_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create the cars."""
        new_car = Turtle(shape="square")
        new_car.color("black", random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(x=random.randint(-280, 1000), y=random.randint(-240, 240))

        return new_car

    def create_all_cars(self):
        """Adds the cars to a list until 100 cars are made."""

        for _ in range(50):
            self.cars_list.append(self.create_car())

    def move(self):
        """Moves the cars."""

        for car in self.cars_list:
            car.back(self.movement_speed)

    def reset(self):
        """Resets the position of the car so that it may be reused."""

        for car in self.cars_list:
            if car.xcor() <= -300:
                car.goto(x=random.randint(300, 1000),
                         y=random.randint(-240, 240))

    def speed_up(self):
        """Speed up cars when the level advances"""
        self.movement_speed += 1
