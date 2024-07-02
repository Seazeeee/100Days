# Unlimited Arguments

## \*args: Also known as unlimited positional arguments

Imagine we have an addition function

```python

def add(n1, n2):
    return n1 + n2

```

However, we want to add 3 numbers? How would be go about doing that?

```python

def add(*args):
    total = 0
    for n in args:
        total += n

    return total

```

The really important part of this is to realize that the \* in the reason python realizes that it can have any number of values.

## \*\*kwargs: Many Key-worded Arguments

```python

def calculate(**kwargs):
    # This is a dictionary

    print(kwargs)  # {"add": 3, "multiply": 5}



calculate(add=3, multiply=5)
```

This lets you look for the specific key and find the ones that you want to then do something. So in this case its a calculate function and we do different things based on this key.
