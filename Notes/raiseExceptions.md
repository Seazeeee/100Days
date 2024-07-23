# Raise

Imagine I want to raise a exception regardless of the outcome.

```python

# Above Code

finally:
    raise TypeError("This is an error that I made up.")

```

## When would you want to use this?

Imagine we're getting the BMI of somebody

```python

height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height ** 2

```

What if we gto an input that is not physically possible?

We may want to raise and exception

```python

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2

```
