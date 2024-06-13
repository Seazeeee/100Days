# Slicing

Imagine we have piano keys that go all the way from A -> G.

piano_keys = [a, b, c, d, e, f, g]

We can slice this and only get c -> e.

We would do this by using [:] | piano_keys[2:5] is an example.

```python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])  # C, D, E
```

These slices are useful for getting different values out of list.

Third number after colon sets the step or increment.

Every other item would be.

```python

print(piano_keys[::2]) #  Every other one

print(piano_keys[::-1]) #  This goes from the end of the list.
```

> This also works for TUPLES!
> You can use the same way of slicing

