"""Creating a snake game."""

import time  # To slow down the snake.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set the screen settings.
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)  # Removes animations | Have to use SCREEN.update().

# Creating the necessary variables needed for game.
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True


SCREEN.listen()  # Declare the listener

# Creating the 4 different movement keys
SCREEN.onkey(snake.up, "Up")  # IMPORTANT: Dont use ()
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")

# Creating a for loop that keeps the game running until a condition.
while game_is_on:
    SCREEN.update()  # Updated the screen.
    time.sleep(0.4)  # Making the snake move at a good pace.
    snake.move()  # Calling the move function that moves the snake.

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()
    
    # Detect tail collision


SCREEN.exitonclick()
