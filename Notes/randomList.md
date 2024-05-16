# Random Library

Biggest category for randomness is *Games*

Computers are Deterministic | They perform *repeatable actions in a predictable way*

Theres a bunch of math to make computers create randomness

Python uses - [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)

# Example

Great python resource when lost | [Ask Python!](https://www.askpython.com/)

```python

import random #Brings in the random module

random_integer = random.randint(1, 10)

print(random_integer) #Will generate a *random* number between the range specified


```

# Modules

Small bits of code that are used for complicated python files
 - Imagine a car - multiple people work on different parts ( tires, wheels, chassis, engine) which are then combined after.

> Creating our own
> Create a new python file | This will all be explained in [rps](../Projects/rps/)

## Random Float #s


```python

import random #Brings in the random module

random_integer = random.randint(1, 10)

print(random_integer) #Will generate a *random* number between the range specified

random_float = random.random() # 0.0 - 1.0 | Does not include 1.0
print(random_float)

# 0.0 - 5

random_float * 5 # | Does not include 5


```

# List | IMPORTANT!!!

Data Structure - A way to organize and store data

List are always [] and items are separated by ,'s

Example
```python

fruits = ["Cherry", "Apple", "Pear"]
```

### US States Example

```python
#Index              0             1          ->
states_of_US = ["Delaware", "Pennsylvania", ...] 

print(states_of_US[0]) #Prints out the given index of list item

# This is also important
print(states_of_US[-1]) # | Moves from the back of the list: 1 being the last item 

# Change items in a list

states_of_US[1] = "Pecilvania"

# Imagine another state is added

states_of_US.append("Heaven") # This adds an item to the end of the list

```

There is a whole list of more functions associated to list 
- Find them here [Python List Doc](https://docs.python.org/3/tutorial/datastructures.html)
- Reading documentation is key to understanding a new data type or module!!

```python
#Index              0             1          ->
states_of_US = ["Delaware", "Pennsylvania", ...] 

print(states_of_US[0]) #Prints out the given index of list item

# This is also important
print(states_of_US[-1]) # | Moves from the back of the list: 1 being the last item 

# Change items in a list

states_of_US[1] = "Pecilvania"

# Adding another list into our list

states_of_US.extend(["Earth", "Space"]) # Adds to the end of the list

```

Programming should be seen as a open book exam | It is encouraged to look and read through documentation!!!!!

### Index out of Range

> Probably the most common issue

The len function returns 50 however it starts at 0, so there is 49
Going outside of the [50] gives and out of range error 

```python

num_of_states = len(states_of_US)

print(states_of_US[num_of_states]) #Out of range because its 50

# IT IS COMMON TO HAVE A -1

print(states_of_US[num_of_states]-1)

```

### Seperate List out into Categories

```python

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# You could create two list however, they share a relation

fruits = [...]
vegetables = [...]

### Nested List

dirty_dozen = [fruits, vegetables]

# [[list1], [list2]]

```
