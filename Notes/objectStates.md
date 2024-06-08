# Object States and Instances

We know how to build one turtle from the class. How do we make more?

- We can use a class to define what a turtle can appear like and how it should behave
- This would create a object that performs these actions

Object - Class
timmy = Turtle()
tommy = Turtle()

We can create as many of these as we need however. Even though they are the same object
they operate completely separate from each other. These are called instances

That means that both objects could be doing different things at the same time.

timmy.color = green
tommy.color = purple

The above is considered state. The state of timmy's color is green and tommy's is
purple. This is true for each different functions and methods.