"""Basic calculator based on user input using functions"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


value1 = float(input("Please enter the first number: "))
operator = input("Please enter the operation (+, -, *, /): ")
value2 = float(input("Please enter the second number: "))

if operator == "+":
    print(f"{value1} + {value2} = {add(value1, value2)}")
elif operator == "-":
    print(f"{value1} - {value2} = {subtract(value1, value2)}")
elif operator == "*":
    print(f"{value1} * {value2} = {multiply(value1, value2)}")
elif operator == "/":
    print(f"{value1} / {value2} = {divide(value1, value2)}")
else:
    print("Error: Enter a valid operator")
