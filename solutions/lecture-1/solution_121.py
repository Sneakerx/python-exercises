"""BMI computation upon user input"""

my_height = float(input("Please enter your height in meters: "))
my_weight = float(input("Please enter your weight in kg: "))

bmi = my_weight / (my_height**2)

print(f"Your bmi is {bmi:.2f}")
