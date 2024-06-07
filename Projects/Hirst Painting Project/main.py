"""To create a Hirst like Color dot painting with turtle"""

# import colorgram
import random
from turtle import Turtle, Screen


CASPER = Turtle()
SCREEN = Screen()


# def get_color() -> list:
#     """
#     Gets colors from provided images and returns a list of tuples
#     that contain the RGB values.
#     """

#     colors = colorgram.extract("Projects/Hirst Painting Project/Image.jpg", 30)

#     final_rgb = []

#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         rgb = (r, g, b)
#         final_rgb.append(rgb)

#     return final_rgb


# Requirements:
# 10x10
# Each dot is 20 and spaced apart 50
color_list = [
    (249, 249, 248),
    (251, 249, 250),
    (202, 172, 108),
    (222, 228, 234),
    (238, 245, 242),
    (153, 180, 196),
    (152, 186, 174),
    (193, 161, 176),
    (214, 204, 112),
    (208, 179, 195),
    (174, 188, 213),
    (161, 213, 187),
    (162, 203, 214),
    (114, 123, 186),
    (175, 161, 73),
    (214, 181, 180),
    (98, 98, 98),
    (44, 44, 44),
    (199, 208, 42),
    (98, 96, 97),
    (89, 92, 91),
    (20, 22, 22),
    (38, 36, 37),
    (105, 111, 144),
    (66, 63, 64),
    (66, 64, 60),
]
SCREEN.colormode(255)
CASPER.speed("fastest")
SCREEN.screensize(10, 10)
CASPER.penup()
CASPER.hideturtle()
CASPER.goto(-250, -250)

for _ in range(100):
    CASPER.begin_fill()
    selected_color = random.choice(color_list)
    CASPER.fillcolor(selected_color)
    CASPER.circle(20)
    CASPER.forward(50)
    CASPER.end_fill()

    if round(CASPER.xcor()) == 250:
        CASPER.goto(-250, (CASPER.ycor() + 50))

SCREEN.exitonclick()
