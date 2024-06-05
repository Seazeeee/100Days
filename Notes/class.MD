# Classes

## How can we create our own classes?

Different Naming Convention

- PascalCase

- camelCase 

- snake_case

```python

class User:
    
    # This will be called every time we create a object or "new user"
    def __init__(self, user_id, username):
        self.id = user_id
        # It is convention to make the name of the parameter the same as the attribute 
        self.username = username
        self.followers = 0 # A default value that doesn't need to be provided
        self.following = 0
    
    # A method always needs a "self" parameter
    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Matt")

user_2 = User("002", "Jack")

# Returns the id that we fed to the constructor. It is important to know
# That this class now requires these 2 parameters

```
### Constructor

This is a part of the blueprint that allows us to specify what should happen when we 
call our object. Also known as initializing,

```python

class Car:
    def __init__(self): # __term__ means its a unique function that python realizes
        #Initialize attributes

```
#### How do we set attributes?

- Self means itself or the object

```python

class Car:
    def __init__(self, seats): # __term__ means its a unique function that python realizes
        #Initialize attributes
        self.seats = seats

my_car = Car(5) # We can pass in data to set the attributes for that object
my_car.seats = 5 # these two terms are equal
# These are attributes which are attached to objects.Instead of declaring these attributes
# each time we can instead put it inside of our class.

```

### Methods

- The thing the objects does

```python

class Car:
    def __init__(self, seats): # __term__ means its a unique function that python realizes
        #Initialize attributes
        self.seats = seats

    def enter_race_mode():
        self.seats = 2

my_car.enter_race_mode():

```