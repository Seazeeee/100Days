import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.title("Turtle Crossing Game")
SCREEN.tracer(0)

# Setting the necessary variables.
SCREEN.listen()
player = Player()
cars = CarManager()

SCREEN.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    SCREEN.update()
    cars.move()
    cars.reset()

SCREEN.exitonclick()
