# Overflow

An overflow drain can be visualized as a conditional statement

*IF* {Water Level > 80cm, then drain water, else continue}

The above is an example of a if/else statement

PYTHON EXAMPLE:

if *condition* is true:
    do this
else *condition* is false:
    do this


```python
water_level = 50

if water_level > 80:
    print("Drain Water")
else:
    print("Continue")
```

# Rollercoaster height Example
- Remember that indentation is important.

```python

print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm?" ))

if height >= 120:
    print("You can ride this rollercoaster!")
else:
    print("You cannot ride this ride.")

```

- Now lets check for their age as well | This will calculate the amount they should pay.

# Nested if/else

if *condition* is true:
    if another *condition* is true:
        do this
    else another *condition* is false:
        do this
else *condition* is false:
    do this


```python

print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm?" ))

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("What is your age?" ))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You cannot ride this ride.")

```

# if / elif / else


```python

print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm?" ))

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("What is your age?" ))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You cannot ride this ride.")

```

# Multiple If statements in succession

- Checks for all conditions | Executes all if statements

if *condition* is true:
    do this
if *condition 2* is also true:
    do this
if *condition 3*:
    do this


# Rollercoaster Example

```python

print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm?" ))

bill = 0

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("What is your age?" ))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth Tickets are $7.")
        bill = 7
    else:
        print("Adult Tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N.")

    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3
    
    print(f"Your final bill is ${bill}")

else:
    print("You cannot ride this ride.")

```

# Multiple Conditions

Logical Operators

*And* | Both have to be true otherwise false
*Or* | Either can be true only false when both are not true
*Not* | It flips ie. True becomes False and False becomes True

```python

print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm?" ))

bill = 0

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("What is your age?" ))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth Tickets are $7.")
        bill = 7
    elif age >= 45 or <= 55:
        print("You can ride free today!")
    else:
        print("Adult Tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N.")

    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3
    
    print(f"Your final bill is ${bill}")

else:
    print("You cannot ride this ride.")

```