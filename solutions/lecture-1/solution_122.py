"""Pythagorean theorem: calculator for the hypotenuse of a right triangle"""

a = float(input("Please enter the length of side a: "))
b = float(input("Please enter the length of side b: "))
c = (a**2 + b**2) ** 0.5
print(f"The length of side c is {c}")
