# Scopes

If you have an apple tree in your yard with a fence. Only you and your family can access it
When there is an apple tree in the neighborhood it is free game for anyone.

```python
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # Prints 2

increase_enemies()
print(f"enemies outside function: {enemies}") # Prints 1

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)
# You can only use the variable within the function.

# Global Scope

player_health = 10 # Available anywhere in our file

def drink_potion2():
    potion_strength = 2
    print(player_health)

drink_potion2()

```

### Anything you give a name has a 'namespace'

# Block Scope

There is no Block Scope in Python

```python

if 3 > 4:
    count += 1

# This does not count as a fence

```

# Global Scope

Modifying Global Scope | This is a bad idea
Avoid modifying global scope

A Way to do this is to return it

```python

enemies = 1 # Global

def increase_enemies():
    print(f"enemies inside function: {enemies}") # Prints 2
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}") # Prints 1

```

# Global Constants

Variables you define and are never going to change again

Ex. 

```python

# Proper naming is to make sure constants are all upper_case

PI = 3.14159
URL = "https://www.google.com"
