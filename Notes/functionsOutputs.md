# More on functions

### Functions with Output

Example:
```python
def my_function():
    return 3 * 2

output = my_function() # Will return the results = result

# Functions with Outputs

def format_name(f_name, l_name):

    '''
    angela
    ANGELA
    aNGEla
    '''

    f_name_title = f_name.title()
    l_name_title = l.name.title()

    return f"{f_name_title} {l_name_title}"
    # You can't add a line after the return


print(format_name("maTT", "THo"))

# output = len("Matt")
# # |         |
# # Input     Output
```

# Return

You can have multiple returns in a function
However, code is not executed after a return
Think of it as a "break"

```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        # Checks for valid inputs
        return "You didn't provide valid inputs. 

    f_name_title = f_name.title()
    l_name_title = l.name.title()

    return f"{f_name_title} {l_name_title}"
    # You can't add a line after the return
```

# Docstrings

Documentation that you can add to code. It is what tells you what a function does.
Can also use it as a multi-lined comment.
Python recommends that you don't do this!!

```python
def format_name(f_name, l_name):
    """
    Take a first and last name and format it to 
    return the title case version of the name.
    """
    if f_name == "" or l_name == "":
        # Checks for valid inputs
        return "You didn't provide valid inputs. 

    f_name_title = f_name.title()
    l_name_title = l.name.title()

    return f"{f_name_title} {l_name_title}"
    # You can't add a line after the return

format_name() # Shows documentation
```