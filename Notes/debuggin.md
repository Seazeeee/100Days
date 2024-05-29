# Debugging

Grace Hopper was the first person to find a real bug inside of her computers that was 
preventing her code from running

### Everyone creates bugs.

Tips and tricks!

- Describe the Problem!
- Reproduce the Bug
- Play Computer
- Fix the Errors ( Red Lines )
- Print is Your Friend
- Use a Debugger

```python
############DEBUGGING#####################

# Describe Problem

# The while loops is looping through 1-20 and when i hits 20 it is suppose to print out
# "You got it". This doesn't work because python does not include the final number in its
# Range. So the loop itself is only going from 1-19. Increasing the range to (1, 21) 
# Should solve our issues!

def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug

# This is a bug with the index given within randint. We are forcing randint to be between
# (1, 6). This works for human brains but dice_imgs.length() would return 5 because
# computer start indexing at 0. We can fix this bug by changing randint to (0, 5).

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer

# If year == 1994 it returns nothing. This is because we have no case that includes 1994
# The way we can fix this is by making year <= 1994 instead of year < 1994. 

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

#Print is Your Friend

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger

# Breakpoint. Lets you tell the debugger to stop so you can examine all the different 
# variables and what their values are. We need to tab the append into the for loop so it
# adds each item.

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

```

### Final Tips

- Take a break
It is important to take a break and let your brain have some downtime

- Ask a Friend
Having fresh eyes makes it easier for the bug to be spotted

- Run Often
Run your program often. It is important to make sure you confirm that the program is doing
what you want it to do after every change. Always tackle bugs one at a time

- Ask StackOverflow
It is important to use this as a tool to research and search for your issue. If you think
that nobody has never seen your problem before you may want to ask a question.