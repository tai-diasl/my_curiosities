# Creating a calculator

print("""
| --  Calculator  --  |
 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

# Functions


def func_sum():
    res = num1 + num2
    print(f"Result: {num1} + {num2} = {res}")


def func_sub():
    res = num1 - num2
    print(f"Result: {num1} - {num2} = {res}")


def func_mult():
    res = num1 * num2
    print(f"Result: {num1} * {num2} = {res}")


def func_div():
    res = num1 / num2
    print(f"Result: {num1} / {num2} = {res}")


def func_whole_div():
    res = num1 // num2
    print(f"Result: {num1} // {num2} = {res}")


def func_exp():
    res = num1 ** num2
    print(f"Result: {num1} ** {num2} = {res}")


# Program
answer = "yes"

while answer == "yes":

    print("What operation would you like to choose?")

    print("1. SUM")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. WHOLE DIVISION")
    print("6. EXPONENTIATION")

    operation = int(input("\nEnter the option number: "))

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if operation == 1:
        func_sum()
    elif operation == 2:
        func_sub()
    elif operation == 3:
        func_mult()
    elif operation == 4:
        func_div()
    elif operation == 5:
        func_whole_div()
    elif operation == 6:
        func_exp()
    else:
        print("INVALID option!")

    answer = input("\nWould you like to do another operation? [yes/no]? ").lower()

print("\nThank you for using our Calculator.")
print("Finished program.")
