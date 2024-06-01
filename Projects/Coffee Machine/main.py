"""A coffee machine made inside of python that uses data to create and
dispense a drink if the proper currency is given."""

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

    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): "
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
    # Checks if user input is off. Results in exiting the program/
    if user_input == "off":
        print("Turning the machine off.")
        sys.exit()


def report(user_input):
    """Returns a report on all resources

    Args:
        user_input (str): the choice made by the user.
    """

    # Checks if user input is report. Displays all items from resources.
    if user_input == "report":
        for key, value in resources.items():
            if key == "money":
                print(f"{key.title()}: ${value:.2f}")
            else:
                print(f"{key.title()}: {value}")
        return True


def add_money(amount):
    """Adds the amount of money to the dictionary

    Args:
        amount (float): the amount of money inserted
    """

    # Adds money resources with the given amount
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


def payment_calc(user_input):
    """A calculation of payment based on selected item

    Args:
        user_input (str): users selected item.
    """

    print("Please insert coins.")

    currency_amount = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01,
    }

    selected_item = MENU[user_input]

    needed_amount = selected_item["cost"]

    quarters, dimes, nickels, pennies = ask_for_coins()

    final_quarters = quarters * float(currency_amount["quarter"])
    final_dimes = dimes * float(currency_amount["dime"])
    final_nickels = nickels * float(currency_amount["nickel"])
    final_pennies = pennies * float(currency_amount["penny"])

    total_paid = final_quarters + final_dimes + final_nickels + final_pennies

    if total_paid < needed_amount:
        print("Sorry that's not enough money." + " Money Refunded.")
        return

    final_amount = float(needed_amount) - total_paid

    if final_amount < 0:
        print(f"Here is  ${final_amount * -1:.2f} in change.")

    print(f"Here is your {user_input} ☕. Enjoy! ")

    resources["money"] += needed_amount

    reduce_resource(user_input)


def process_payment(user_input):
    """Calls the calculation function to calculate payment based on selection.

    Args:
        user_input (str): users selected item.
    """

    if user_input == "espresso":

        payment_calc(user_input)

    elif user_input == "latte":

        payment_calc(user_input)

    elif user_input == "cappuccino":

        payment_calc(user_input)


def ask_for_coins():
    """Ask the user to insert the coins.

    Returns:
        int: the different amount of coins inserted.
    """

    quarters = int(input("How many quarters?: "))

    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    return quarters, dimes, nickels, pennies


def reduce_resource(user_input):
    """Removes the resources from the given storage.

    Args:
        user_input (str): users selected item.
    """

    selected_item = MENU[user_input]

    needed_ingredients = selected_item["ingredients"]

    for key, value in needed_ingredients.items():

        resources[key] -= value


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
        reports = report(choice)

        if reports:
            continue

        # If neither 'secret' options are selected go into if statements
        # to make sure resources and payment are processed.

        have_resources = have_resource(choice)

        if have_resources:

            process_payment(choice)

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


if __name__ == "__main__":

    machine()
