# import random #Brings in the random module
# # import example_module

# random_integer = random.randint(1, 10)

# print(random_integer) #Will generate a *random* number between the range specified

# # print(example_module.pi)

import random

"""
    TODO

    Create a Rock, Paper, Scissors game with the computer

    Combinations:
        Rock vs. Rock: Draw - Done
        Rock vs. Paper: Paper wins - Done
        Rock vs. Scissors: Rock wins - Done
        Paper vs. Rock: Paper wins - Done
        Paper vs. Paper: Draw - Done
        Paper vs. Scissors: Scissors win - done
        Scissors vs. Rock: Rock wins - Done
        Scissors vs. Paper: Scissors win - Done
        Scissors vs. Scissors: Draw - Done

"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

if user_choice < 0 or user_choice >= 3:
    print("You used an invalid number. Try again!")
    exit()
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chose: ")
print(game_images[computer_choice])


# Checking all possible combinations for results

# Check our user_choice

if user_choice == 0 and computer_choice == 0:
    print("It's a Draw!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 1:
    print("It's a Draw!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Its a Draw!")