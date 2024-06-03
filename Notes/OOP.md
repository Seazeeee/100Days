# Object-Oriented Programming

### Procedural Programming

A style of programming where you create functions that lead to other functions. 
Normally, works from top to button and jumps to a function when needed.
Older languages relied on this exclusively.

How can we maintain a simple style of code while making them more complex?

### Object-Oriented Programming

If we split up big task into smaller modules more people can work on the same project.
Many of these modules can be re-used if needed. Re-using code is beneficial for this.

- What is it?

Imagine you are tasked with running a restaurant. Think about all the different roles you
would have to do. Server, Chef, cleaner, etc.

You cannot create a large, complex project if we are using procedural style programming.

### The Alternative

Imagine we hired people for each individual role. This way we can manage all of our staff
in the restaurant without working about all the miniscule details.

We can use this same concept to simplify the relationships within our code.

#### How to use it?

So if we hired a chef, waiter, and cleaner. We would then be the manager.

If this was a program we would have to model all of these roles.

- Think about what is has:
- Think about what is does:

An attribute is just a fancy word for a variable that is attached to a particular object.
In this example that would be waiter.

A Method is a function that a particular object can do. This is the same object as
attributes.

Example:
```python

# Attributes:
is_holding_plate = True
tables_responsible = [4, 5, 6]

# Methods:
def take_order(table, order):
    # Takes order to chef
    
def take_payment(amount):
    # Add money to restaurant

```
In OOP we're trying to model real life objects that they have ( attributes ) and the 
things that they can do ( methods ).

We can have multiple objects that are created from the same type. This way we could create
2 waiters.

- Henry
- Betty

These can use the same blueprint ( class ). The generated item from a class is called an
object.

# Constructing Objects

The class is the blueprint that is modeling a real life object. Using the blueprint you 
can create as many object as your want

```python
#Object     #CLass
  car = CarBlueprint()

```
We are going to be using a library of code to start making GUIs.
We can use others blueprints and classes
The library we will be using is Turtle Graphics

Car Attributes:
- speed = 0
- fuel = 32

To access the attributes | 
```python
#Object | Attribute
car.speed
```

Car Methods:
- move()
- stop()

```python

car = CarBlueprint()

def move():
    speed = 60

def stop():
    speed = 0

#Object | Method
car.stop()
```

### Python Packages

A package is a whole bunch of code that other people have written. Lets say we wanted to
make a database with pokemon. We can search for a package on [pypi](pypi.org).





