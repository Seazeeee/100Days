"""Creating a snake game."""

from turtle import Screen, Turtle
import time  # To slow down the snake.

# Set the screen settings.
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)  # Removes animations | Have to use SCREEN.update().

# Creating the necessary variables needed for game.
dict_turtles = {}
cords = [(0, 0), (-20, 0), (-40, 0)]
game_is_on = True


for num_index, position in enumerate(cords):
    # Create the different turtle methods needed; adds them to a dict.
    dict_turtles[num_index] = Turtle(shape="square")
    dict_turtles[num_index].penup()
    dict_turtles[num_index].color("white")
    dict_turtles[num_index].goto(cords[num_index])

# Creating a for loop that keeps the game running until a condition.
while game_is_on:
    SCREEN.update()  # Updated the screen.
    time.sleep(0.1)  # Making the snake move at a good pace.
    for num_turtle in range(len(dict_turtles) - 1, 0, -1):
        # Grab the front turtle and its cords.
        forward_turtle = dict_turtles[num_turtle - 1]
        new_x = forward_turtle.xcor()
        new_y = forward_turtle.ycor()
        # Move the turtle behind to the new cords.
        dict_turtles[num_turtle].goto(x=new_x, y=new_y)


SCREEN.exitonclick()
