# Import sys to exit program
import sys

# Import data to maintain and monitor resources
from data import MENU, resources


# Prompt the user by asking what they would like.


def prompt_user():
    """Prompts the user to select their drink option

    Returns:
        str: returns selected option
    """

    # Create a variable for user input.

    user_choice = input("What would you like? (espresso/latte/cappuccino): "
                        ).lower()

    # Checks the input; returns the corresponding string
    if user_choice == "espresso":
        return "espresso"

    elif user_choice == "latte":
        return "latte"

    elif user_choice == "cappuccino":
        return "cappuccino"

    else:
        return user_choice


def off(user_input):
    """Turns the machine off if given the right condition

    Args:
        user_input (str): the choice made by the user.
    """
    if user_input == "off":
        print("Turning the machine off.")
        sys.exit()


def report(user_input):
    """Returns a report on all resources

    Args:
        user_input (str): the choice made by the user.
    """

    if user_input == "report":
        for key, value in resources.items():
            if key == "money":
                print(f"{key.title()}: ${value}")
            else:
                print(f"{key.title()}: {value}")


def add_money(amount):
    """Adds the amount of money to the dictionary

    Args:
        amount (float): the amount of money inserted
    """

    resources["money"] += amount


def have_resource(user_input):
    """Checks to validate that there are enough resources available
    to make the drink.

    Args:
        user_input (str): the choice made by the user.

    Returns:
        boolean: return true if there are enough resources else returns
        false if they're not enough resources.

        resources_key (str): the missing ingredient.
    """

    if user_input == "espresso":

        # Check to make sure resources are sufficient

        selected_item = MENU[user_input]

        needed_ingredients = selected_item["ingredients"]

        for ingredients_keys, ingredients_value in needed_ingredients.items():
            for resources_key, resources_value in resources.items():
                if ingredients_keys == resources_key:
                    if resources_value < ingredients_value:
                        return False
        return True

    elif user_input == "latte":
        # Check to make sure resources are sufficient

        selected_item = MENU[user_input]

        needed_ingredients = selected_item["ingredients"]

        for ingredients_keys, ingredients_value in needed_ingredients.items():
            for resources_key, resources_value in resources.items():
                if ingredients_keys == resources_key:
                    if resources_value < ingredients_value:
                        return False
        return True

    elif user_input == "cappuccino":
        # Check to make sure resources are sufficient

        selected_item = MENU[user_input]

        needed_ingredients = selected_item["ingredients"]

        for ingredients_keys, ingredients_value in needed_ingredients.items():
            for resources_key, resources_value in resources.items():
                if ingredients_keys == resources_key:
                    if resources_value < ingredients_value:
                        return False
        return True


def machine():
    """
    The function that runs the coffee machine.
    """

    # Set resources low to false first
    resources_low = False

    # Set money to 0
    resources["money"] = 0

    while not resources_low:

        choice = prompt_user()

        # Check is input is off
        off(choice)

        # Checks if input is report
        report(choice)

        # If neither 'secret' options are selected go into if statements
        # to make sure resources and payment are processed.

        have_resources = have_resource(choice)

        if have_resources:

            # TODO: Process Payment in terms of coins.

            print("Inside If.")

        else:
            # Use the above function to also grab the missing ingredient.
            selected_item = MENU[choice]

            needed_ingredients = selected_item["ingredients"]

            for ingredients_keys, ingredients_value \
                    in needed_ingredients.items():               
                for resources_key, resources_value in resources.items():

                    if ingredients_keys == resources_key:

                        if resources_value < ingredients_value:

                            lacking_resource = resources_key

            print(f"Sorry there is not enough {lacking_resource}.")


machine()
