# Import data
from given_game_data import data

# import Art
from art import logo, vs

# Create a function that pulls the name, what they do, and location
# From the data. This needs a random choice
import random



def get_random_data():

    # Generates 1 choices
    random_choice = random.choice(data)

    # Grab followers to return
    followers = random_choice["follower_count"]

    # Return the string needed
    return (
        f"{random_choice['name']}, a {random_choice['description']}, from {random_choice['country']}",
        followers,
    )


# Create a function that compares the followers of each choice
def compare_followers(a_follow_count, b_follow_count):

    if a_follow_count > b_follow_count:
        return a_follow_count
    elif b_follow_count > a_follow_count:
        return b_follow_count
    else:
        return None


# Create a function to get choice A
def choice_A():
    a_choice, a_followers = get_random_data()
    print(f"Compare A: {a_choice}")
    print(f"Pssst.... There follower count is: {a_followers}")
    return a_followers


# Create a function to get choice B
def choice_B():
    b_choice, b_followers = get_random_data()
    print(f"Compare B: {b_choice}")
    print(f"Pssst.... There follower count is: {b_followers}")
    return b_followers

# Create a function that replaces previous choice if correct


# Create a main game function that will house the whole thing
def game():
    # Print Logo
    print(logo)

    # Create a score counter
    score_counter = 0
    # Create a while conditional that will run until score_counter == -1
    while score_counter != -1:
        # Create a conditional that prints the score once its above 0
        if score_counter > 0:
            print(f"You're Right! Current score: {score_counter}")

        # Call Choice A
        a_follow = choice_A()

        # Print VS
        print(vs)

        # Call Choice B
        b_follow = choice_B()

        # Call the compare function to see which is higher

        higher_followers = compare_followers(
            a_follow_count=a_follow, b_follow_count=b_follow
        )

        user_choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()

        if user_choice == "a" and higher_followers == a_follow:
            score_counter += 1
        elif user_choice == "b" and higher_followers == b_follow:
            score_counter += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score_counter}")
            score_counter = -1


game()
