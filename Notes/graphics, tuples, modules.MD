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

```

# Importing Modules

- Simple Import
```python

import turtle

tim = turtle.Turtle()
```
- From Import

You can import everything by using an * ( from turtle import *)
Be careful using this because it makes code confusing when you don't have an idea of 
where its coming from.
```python

from turtle import Turtle

# Makes it cleaner to read if we need to use the thing we're
# importing a lot
tim = Turtle()
tom = Turtle()

```

- Aliasing Modules

This allows you to give a module an "alias" name or a name that we defined.
```python

import trutle as t

tim = t.Turtle()
```

# Installing Modules
There are some modules that you can't just import. We may need to install the module
first. We can import turtle because it is package within the python installer. However,
for other modules we need to install them. Think about it like going to a much larger
library to find a new book.

If you run code without the module installed the error will tell you that it can't find
that library. These are normally installed in the .venv folder that is per project.

It is important to work with virtual environments because different versions of python
are not backwards compatible. 