from art import logo
# Add
def add(num1, num2):
    return num1 + num2
# Subtract
def subtract(num1, num2):
    return num1 - num2
# Multiply
def multiply(num1, num2):
    return num1 * num2
# Divide
def divide(num1, num2):
    return num1 / num2
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations.keys():
        print(key)
    continue_bool = True
    while continue_bool:
        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("What's the next number?: "))
        calculation_operation = operations[operation_symbol]
        answer = calculation_operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: "
            )
            == "y"
        ):
            num1 = answer
        else:
            continue_bool = False
            calculator()
calculator()
