# Python Turtle

A way to draw graphics onto the screen. Think of a turtle with a pen on its back so that
when it moves it leaves drawings behind.

Developers use documentation to figure out how to use and understand these modules. This
is why we know how the modules work. It is also ok to use stackoverflow to search for help
when using modules. It is better to use google.com then stackoverflow itself when
searching.

### Graphical User Interface
- Also known as GUI

Before this we had text-based interfaces. Tkinter is what the turtle module relies on when
creating the graphics. Tkinter stands for TK-interface.
```python

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("black")



# This needs to happen at the end
screen = Screen()
screen.exitonclick()
