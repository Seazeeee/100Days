from turtle import Turtle, Screen

SCREEN = Screen()
SCREEN.setup(width=500, height=400)
user_choice = SCREEN.textinput(
    title="Make your bet.",
    prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
dict_turtles = {}
y_start = -100

for color in colors:
    dict_turtles[color] = Turtle(shape="turtle")
    dict_turtles[color].penup()
    dict_turtles[color].color(color)
    dict_turtles[color].goto(x=-230, y=y_start)
    y_start += 40

SCREEN.exitonclick()
