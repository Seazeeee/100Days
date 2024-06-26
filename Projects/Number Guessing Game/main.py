# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random


def random_number():
    return random.randint(1, 100)


def num_lives(difficulty):

    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        return f"You have not provided a valid input for your difficulty, try again!"


def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    selected_number = random_number()

    difficulty_choice = str(
        input("Choose a difficulty. Type 'easy' or 'hard': ")
    ).lower()
    lives = num_lives(difficulty_choice)

    while lives > 0:

        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess > selected_number:
            print("Too High.")
            if lives == 1:
                lives -= 1
                continue
            else:
                lives -= 1
                print("Guess again.")
                continue

        elif user_guess < selected_number:
            print("Too low.")
            if lives == 1:
                lives -= 1
                continue
            else:
                lives -= 1
                print("Guess again.")
                continue

        else:

            print(f"You got it! The answer was {selected_number}")
            break

    if lives == 0:
        print("You have run out of guesses, you lose.")


if __name__ == "__main__":
    game()