"""Module that handles the main method for the game."""
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
scoreboard = Scoreboard()

SCREEN.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    SCREEN.update()
    cars.move()
    cars.reset()

    # Checks for win.
    if player.win():
        scoreboard.increase_score()
        cars.speed_up()
        print(cars.movement_speed)

    # Checks for player and car collision
    for car in cars.cars_list:
        if car.distance(player) <= 23.5:
            # Print GAME OVER with SCOREBOARD
            scoreboard.game_over()
            SCREEN.mainloop()
            game_is_on = False

SCREEN.exitonclick()
