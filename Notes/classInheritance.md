# Class Inheritance

If you code up a class called chef with a lot of methods.

However, you realized you need a pastry chef as well. You can then take the methods from
chef and add onto it for the pastry chef. This class "inherits" methods from another 
class. 

```python
# Before Inheritance
class Fish:
    def __init__(self):

# After Inheritance
class Fish(Animal):
    def __init__(self):
        super().__init__()  
```

Super refers to the "super" class

```python

class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
    

class Fish(Animal):

    def __init__(self):
        super().__init__()


    def swim(self):
        print("moving in water.")
    

nemo = Fish()
nemo.swim()  # Moving in water.
nemo.breathe()  # Inhale, exhale.
```

This makes it so the fish class can access all the methods from the animal class.

### How do we modify it?

```python
class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
    

class Fish(Animal):

    def __init__(self):
        super().__init__()
    
    
    def breathe(self):
        super().breathe()  # Do everything from the super class
        print("doing this underwater.")  # Edited for the fish class.


    def swim(self):
        print("moving in water.")
    

nemo = Fish()
nemo.swim()  # Moving in water.
nemo.breathe()  # Inhale, exhale.