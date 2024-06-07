from turtle import Turtle, Screen
import random

casper = Turtle()
MY_SCREEN = Screen()


def random_color():
    """A method that returns a random RGB tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

# First Challenge: Draw a square.
# for _ in range(4):
#     casper.forward(100)
#     casper.right(90)

# Second Challenge: Dotted Line
# for _ in range(15):
#     casper.forward(10)
#     casper.penup()
#     casper.forward(10)
#     casper.pendown()

# Third Challenge:
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon, and decagon.

# side_count = 3
# goal_side = 10
# while side_count < goal_side:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     MY_SCREEN.colormode(255)
#     casper.color(r, g, b)
#     for _ in range(side_count):
#         angle = 360 / side_count

#         casper.forward(100)
#         casper.right(angle)
#     side_count += 1
# MY_SCREEN.exitonclick()


# Fourth Challenge:
# Draw a random walk

# Based on the mathematical object.

# for _ in range(200):

#     angles = [0, 90, 180, 270]
#     MY_SCREEN.colormode(255)
#     casper.color(random_color())
#     casper.pensize(10)
#     casper.speed(8)
#     casper.forward(30)
#     casper.setheading(random.choice(angles))

# MY_SCREEN.exitonclick()

# Challenge 5:
# Make a SPirograph
def draw_spirograph(size_of_gaps):
    """Draws a spirogrpah with random colors."""
    for _ in range(int(360/size_of_gaps)):
        MY_SCREEN.colormode(255)
        casper.color(random_color())
        casper.speed("fastest")

        casper.circle(100)
        casper.setheading(casper.heading() + size_of_gaps)


draw_spirograph(5)


MY_SCREEN.exitonclick()