"""
Implement a simple banking application that allows users to deposit and withdraw money,
as well as check their balance. Modify the provided code to store the balance in a file.
"""

import sys


def deposit(balance):
    """deposit money into the account."""
    deposit_amount = float(input("How much money do you want to deposit?"))
    if is_non_positive_number(deposit_amount):
        return balance

    balance += round_to_two_decimals(deposit_amount)
    return balance


def withdraw(balance):
    """withdraw money from the account."""
    withdraw_amount = float(input("How much money do you want to withdraw?"))

    if is_non_positive_number(withdraw_amount):
        return balance

    if withdraw_amount > balance:
        print("Sorry, you don't have enough cash")
        return balance

    balance -= round_to_two_decimals(withdraw_amount)
    return balance


def show_balance(balance):
    """display the current balance."""
    print(f"Your current balance is {balance:.2f}€")


def store_balance(balance):
    """store the current balance in a file."""
    with open("bank_balance.txt", "w", encoding="utf-8") as f:
        f.write(str(balance))


def exit_system(balance):
    """exit the banking system after storing the balance."""
    store_balance(balance)
    print("Bye")
    sys.exit()


def round_to_two_decimals(number):
    """round a number to two decimal places."""
    return round(number, 2)


def is_non_positive_number(number):
    """check if a number is non-positive."""
    if number <= 0:
        print("The amount must be positive.")
        return True
    return False


def main():
    """main function to run the banking application."""
    with open("bank_balance.txt", "r", encoding="utf-8") as f:
        balance = float(f.read())

    # Main loop to handle user input
    while True:
        user_input = input(
            "Please choose an action (1: Deposit, 2: Withdraw, 3: Show Balance, 4: Exit): "
        )

        if user_input == "1":
            balance = deposit(balance)
        elif user_input == "2":
            balance = withdraw(balance)
        elif user_input == "3":
            show_balance(balance)
        elif user_input == "4":
            exit_system(balance)
        else:
            print("Invalid input, please try again")


main()
