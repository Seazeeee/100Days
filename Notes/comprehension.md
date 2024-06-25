# List Comprehension

This is unique to the python language.

Creates a new list where each number is increased by one.

Previously we would've used a for loop.

```python

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

```

Instead we can use list comprehension

```python

new_list = [new_item for item in list]

```

Now lets replace this with the above keywords

```python

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

```

You can also work with other data types.

```python

name = "Angela"

new_list = [letter for letter in name]

```

## Python Sequences

- List
- Range
- String
- Tuple

When you perform a list comprehension; it will go through it in order and then it will take each of those items and do something with them.

Range Ex:

```python

range_list = [n * 2 for n in range(1, 5)]

```

## Conditional List Comprehension

This takes our keywords farther.

```python

new_list = [new_item for item in list if test]

```

Imagine we have a list of names and we only want the names that are length 4 or less.

Ex:

```python

short_names = [name for name in names if len(name) >= 4]

```

Long name Ex:

```python

long_names = [name.upper() for name in names if len(name) >= 5]

```

