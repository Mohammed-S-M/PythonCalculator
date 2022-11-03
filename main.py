# importing logo, PythonCalc class, and clear function.
from art import logo
from os import system, name
from calculator import PythonCalc


# clear function to clear the console.
def clear():
    # for windows.
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix').
    else:
        _ = system('clear')
# end of clear function.


# application main function.
def calculator():
    clear()
    print(logo)
    print("Welcome to PythonCalc.")
    print("This is a simple calculator.")
    print("You can use multiple operators to add, subtract, multiply, and divide.")
    print("-------------------------------------------------------------------------")
    print()
    # asking the user to enter the first value, operator, then the last value.
    first_number = float(input("Enter your first number: "))
    print(type(first_number))
    print("| + | | - | | * | | / |")
    operator = input("Enter your operator: ")
    next_number = float(input("Enter your next number: "))

    # creating the calculation object.
    calc = PythonCalc(first_number, next_number)

    # calculating the total according to the operation.
    total = 0
    if operator == "+":
        total = calc.add()
    elif operator == "-":
        total = calc.subtract()
    elif operator == "*":
        total = calc.multiply()
    elif operator == "/":
        total = calc.divide()

    # printing the final result then asking the user to reset, continue or turn off the calculator.
    print(f"{first_number} {operator} {next_number} = {total}")
    reset_or_continue = input("You want to reset, continue? enter R or C: ").lower()

    # while loop to run the operation again and again until the user turn off the calculator.
    is_continue = True
    while is_continue:
        # if the user chose to reset, then we call the function recursively.
        if reset_or_continue == "r":
            calculator()

        # if the user chose to continue with the calculation,
        # then we ask the user to enter an operator and the next number.
        if reset_or_continue == "c":
            operator = input("Enter your operator: ")
            next_number = float(input("Enter your next number: "))
            continue_calc = PythonCalc(total, next_number)
            new_number = total
            total = 0
            if operator == "+":
                total = continue_calc.add()
            elif operator == "-":
                total = continue_calc.subtract()
            elif operator == "*":
                total = continue_calc.multiply()
            elif operator == "/":
                total = continue_calc.divide()

            print(f"{new_number} {operator} {next_number} = {total}")
            reset_or_continue = input("You want to reset, continue? enter R or C: ").lower()
# end of main function


# calling the main function to start the application
calculator()
