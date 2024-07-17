# Handling Errors & Exceptions

Imagine you try to open a text file that doesn't exists. Naturally, there will be an error.

If this happens somewhere in our program. How would we want to handle it?

We need to plan for these errors because they are more than likely to happen at some point.

## Catching Exceptions

4 Keywords

```python

try:  # Something that might cause an exception

except:  # Do this if there WAS an exception

else:  # Do this if there were no exceptions

finally:  # Do this no matter what happens

```

### FileNotFound

This is an example of how you would handle the above situation.

```python

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
except FileNotFoundError:  # Describes which error to look for
    # Create file
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:  # Catches the a_dict error
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
```
