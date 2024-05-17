# Loops

For Loop

for *item* in *list_of_items*:
  Do something

```python

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

```
Loops for each item of a list etc. and assigns a variable to it

It allows us to execute the same code multiple times.

```python

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie") # Inside

print(fruits) # Outside

# Apple
# Apple Pie
# ...

```
When ever you see a **:** | The indentation is important.
- If indented it means you are inside

# Range

Carl Gauss - Teacher gave him a problem to add all the numbers from 1 - 100

for number in range(a, b):
    print(number)

```python

for number in range(1, 11):
    print(number)
    # Prints 1-9
    # With 1-11 | Prints 1-10
    # You can specify step to make it jump instead of increasing by 1
```

```python

#Gauss Function

total = 0

for number in range(1, 101):
    total += number

print(total) # 5050

```