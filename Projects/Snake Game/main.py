from turtle import Screen, Turtle

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")

dict_turtles = {}
cords = [(0,0), (-20, 0), (-40, 0)]


for num_index, position in enumerate(cords):
    dict_turtles[num_index] = Turtle(shape="square")
    dict_turtles[num_index].penup()
    dict_turtles[num_index].color("white")
    dict_turtles[num_index].goto(cords[num_index])


SCREEN.exitonclick()
