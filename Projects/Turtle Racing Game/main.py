from turtle import Turtle, Screen
import random

is_race_on = False
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

if user_choice:
    is_race_on = True

while is_race_on:
    for name, turtles in dict_turtles.items():
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

        if turtles.xcor() > 230:
            is_race_on = False
            if name == user_choice:
                print(f"You won! {name.title()} won the race!")
            else:
                print(f"You lost! {name.title()} won the race!")


SCREEN.exitonclick()
