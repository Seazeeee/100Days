# File System

## Read and Write

We can use the 'open' method to open the file that is in the same directory
as our main file.

```python

file = open("my_file.txt")

```

File.read() lets you read the contents within the file.

```python

file = open("my_file.txt")
content = file.read()

print(content)

```

_Important_: We have to make sure to close it.

```python

file = open("my_file.txt")
content = file.read()

print(content)
file.close()

```

If you do not close it, the computer will hold it open and use those resources
continuously.

This will auto close the file once we have finished.

```python

with open("my_file.txt") as file:
    content = file.read()

    print(content)

```

### Writing

We can also write text into the file.

This will full write over everything in the file.

```python

with open("my_file.txt", mode = 'w') as file:
    file.write("New text.")

```

If we wanted to append to the text already written we would use a different mode.

```python

with open("my_file.txt", mode = 'a') as file:
    file.write("\nNew text.")

```

If you want to create a new file, this will write it for you!
You just have to make sure the name of the file doesn't exist in the directory.
You also have to be in the "W" mode.

```python

with open("new_file.txt", mode = 'w') as file:
    file.write("\nNew text.")

```

## Paths

There are files and folders.

Files live within folders, and you can have folders nested within one another.

_Absolute File Path_:

These always start with the root. This a path that start from the origin

_Relative File Path_:

What if we are working in the folder above. We call this the working directory.

We can use "./". This means to look inside of this directory. Followed by the path.

We can also use "../" to move up one folder.

