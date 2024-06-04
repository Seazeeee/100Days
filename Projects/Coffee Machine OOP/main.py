"""A Coffee Machine that we previously made using OOP"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def prompt_user():
    """Prompts the user to select their drink option

    Returns:
        str: returns selected option
    """

    # Create a variable for user input.

    user_choice = input(
        f"What would you like? ({menu_items.get_items()[:-1]}) : "
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


# Create Object for Coffee Maker
coffee_Machine = CoffeeMaker()


menu_items = Menu()


payment = MoneyMachine()


is_on = True


while is_on:

    # Prompt user for choice
    choice = prompt_user()

    if choice == "report":
        coffee_Machine.report()
        payment.report()
        continue

    elif choice == "off":
        is_on = False
        break

    menu_choice = menu_items.find_drink(choice)
    if menu_choice:
        if (coffee_Machine.is_resource_sufficient(menu_choice) and
                payment.make_payment(menu_choice.cost)):
            coffee_Machine.make_coffee(menu_choice)
