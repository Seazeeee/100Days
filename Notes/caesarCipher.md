# Caesar Cipher 

When Caesar would send important military messages he would encode them 

### Idea

You would shift the note by 3 units ( A -> D )

# More about Functions

def my_function():
    # Do This
    # Then do this
    # Finally do this

#### Calling the function

my_function()

```python

def greet():
    print("Hello")
    print("My Name is Matt.")
    print("What is yours?")

# Calling the function!
greet()

```

### Modify the function

We can edit what is in the ():

def my_function(something):
    # Do This with something
    # Then do this
    # Finally do this

calling your function

my_function(123)

```python

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Angela")

```
When passing through a variable we are essentially creating a variable.

```python

def my_function(something):
    #Do this with something
```

something  =  123
    |          |
    |          |
Parameter   Argument  

# Positional vs. Keywords

Functions with more than 1 input

```python
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# gree_with("Matt", "Nowhere")

gree_with("Nowhere", "Matt")

#Hello Nowhere
#What is it like in Jack Bauer?
#These are called positional argument

```
# Positional Arguments

def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c

The position of what you enter when calling the function is important

# Keyword Arguments

my_function(a=1, b=2, c=3)

my_function(c=3, a=1, b=2) 

Both of these function calls with have the same results

```python
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# gree_with("Matt", "Nowhere")

gree_with(location="Nowhere", name="Matt")

```

