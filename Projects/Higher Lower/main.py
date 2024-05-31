# Import data
from given_game_data import data

# import Art
from art import logo, vs

# Create a function that pulls the name, what they do, and location
# From the data. This needs a random choice
import random

# Need OS to clear terminal.
import os

# TODO
# Create a way to keep the logo always but remove all text on run


def get_random_data():

    # Generates 1 choices
    random_choice = random.choice(data)

    # Grab followers to return
    followers = random_choice["follower_count"]

    final_string = f"{random_choice['name']}, a {random_choice['description']}, from {random_choice['country']}"

    # Return the string needed
    return final_string, followers


# Create a function that compares the followers of each choice
def compare_followers(a_follow_count, b_follow_count):

    if a_follow_count > b_follow_count:
        return a_follow_count
    elif b_follow_count > a_follow_count:
        return b_follow_count
    else:
        return None


# Create a main game function that will house the whole thing
def game():
    # Create a score counter
    score_counter = 0
    # Call Choice A
    a_string, a_follow = get_random_data()

    # Call Choice B
    b_string, b_follow = get_random_data()

    # Create a while conditional that will run until score_counter == -1
    while score_counter != -1:
        # Clear Terminal
        os.system("clear")

        # Print Logo
        print(logo)

        # Create a conditional that prints the score once its above 0
        if score_counter > 0:
            print(f"You're Right! Current score: {score_counter}")

        # Call Choice A
        print(f"Compare A: {a_string}")
        print(f"Pssst.... There follower count is: {a_follow}")

        # Print VS
        print(vs)

        # Call Choice B
        print(f"Compare B: {b_string}")
        print(f"Pssst.... There follower count is: {b_follow}")

        # Call the compare function to see which is higher

        higher_followers = compare_followers(
            a_follow_count=a_follow, b_follow_count=b_follow
        )

        user_choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()

        if user_choice == "a" and higher_followers == a_follow:
            
            score_counter += 1
            # Get a new Compare B:
            b_string, b_follow = get_random_data()

        elif user_choice == "b" and higher_followers == b_follow:
            score_counter += 1
            # Make Compare B switch to Compare A
            a_string = ""
            # Append B to A
            a_string += b_string

            # Change follower count
            a_follow = b_follow

            # Get a new Compare A
            b_string, b_follow = get_random_data()
        else:
            # Clear Terminal
            os.system("clear")

            # Print Logo
            print(logo)

            print(f"Sorry, that's wrong. Final score: {score_counter}")
            score_counter = -1


game()
