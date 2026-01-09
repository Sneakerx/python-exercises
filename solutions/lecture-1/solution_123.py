"""Basic calculator based on user input"""

value1 = float(input("Please enter the first number: "))
operator = input("Please enter the operation (+, -, *, /): ")
value2 = float(input("Please enter the second number: "))

if operator == "+":
    print(f"{value1} + {value2} = {value1 + value2}")
elif operator == "-":
    print(f"{value1} - {value2} = {value1 - value2}")
elif operator == "*":
    print(f"{value1} * {value2} = {value1 * value2}")
elif operator == "/":
    print(f"{value1} / {value2} = {value1 / value2}")
else:
    print("Error: Enter a valid operator")
