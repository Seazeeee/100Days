# Dictionaries

They work kinda like real dictionaries
- You look up a word and there is a provided definition

One good way to look at a dictionary is a table

| Key | Value |
|-----|-------|
| Bug | An error is a program that prevents the program from running as expected.|
| Function | A piece of code that you can easily call over and over again. |
| Loop | The action of doing something over and over again. |

```python

{Key: Value}

#Multiple Entries
{
    "Bug": "An error is a program that prevents the program from running as expected.,
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

```

### Dictionaries in Action

```python
# It is important to format it properly

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# How to retrieve an item
programming_dictionary["Bug"] #Provide the key | Returns the value

#Add a piece of data
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Empty Dict
empty_dict = {}

# Wipe an existing dictionary
# programming_dictionary = {}

#Edit an item
programming_dictionary["Bug"] = "Changing the value for the key Bug" # | If it doesn't find this key it will create one

#Loop through a dictionary
for key, value in programming_dictionary.items():
    print(key, value)

```

# Nesting

Imagine a folder. Nesting means to put one inside of another.

```python

{
    Key: [List],
    Key2: {Dict},
}

# This is a list and a dictionary "nested" inside of a dictionary

# Samples

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nested List

["A", "B", ["C", "D"]] # Valid but not as useful

# Nested Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"] "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"] "total_visits": 5},
}

# Above is a list nested inside of a dictionary inside of a dictionary

# Nested dictionary inside of a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]