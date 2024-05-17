# Functions

We have already been using multiple functions that are native to python

See [here](https://docs.python.org/3/library/functions.html) for the list of built-in functions.

functions = *name*()

Parentheses means its a function

```python

print("Hello") # This is a print function

num_char = len("Hello") # This a the len function

print(num_char)


```

# How do make our own function?

def my_function():
    # Do this
    # Then Do this
    # Finally do this


```python

def my_function(): #name
    print("Hello")
    print("Bye") 

#To call the function

my_function()

```

# Indentation

Think of a file structure that you see throughout explorer or finder

This is relevant to all previous indention rules we've followed. 

```python

def my_function():

    print("Hello") # Inside of the function
print("World") # Outside of the function

```

### Spaces vs Tabs

Python says that spaces are the preferred indentation method. 

This is going to take years of practice to break. *sigh*

Luckily, IDEs primarily VSCode does this in the background for me!!!!!


# While loop ( IMPORTANT!!! )

Compared to for loop

> for item in list_of_items:
    > do something to each item

> for number in range(a, b):
    > print(number)


while something_is_true:
    #Do something repeatedly

```python

"""
Code used here:
    https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

"""

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6

while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1

```

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
while not at_goal():
    jump()
```

It is not while at_goal() not true but the above.

# When to use which

### For Loops

When you need to do something for each element in something

```python
fruits = ["apple", "pear", "peach"]

for fruit in fruits:
    print(fruit)

```

### While Loop

When you want to carry out a functionality until a condition is met.

You must be careful because while loops can lead to infinite loops.

Printing out your condition can help understand why you're dealing with infinite loops.

```python

#Infinite Loop Example

while 5 > 3:
    #Do this

```

