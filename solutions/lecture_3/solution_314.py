"""
Implement a simple banking application that allows users to deposit and withdraw money,
as well as check their balance. Modify the provided code to store the balance in a file.
"""


def deposit(balance):
    deposit_amount = float(input("How much money do you want to deposit?"))
    if is_non_positive_number(deposit_amount):
        return balance

    balance += round_to_two_decimals(deposit_amount)
    return balance


def withdraw(balance):
    withdraw_amount = float(input("How much money do you want to withdraw?"))

    if is_non_positive_number(withdraw_amount):
        return balance

    if withdraw_amount > balance:
        print("Sorry, you don't have enough cash")
        return balance

    balance -= round_to_two_decimals(withdraw_amount)
    return balance


def show_balance(balance):
    print(f"Your current balance is {balance:.2f}€")


def store_balance(balance):
    with open("bank_balance.txt", "w", encoding="utf-8") as f:
        f.write(str(balance))


def exit_system(balance):
    store_balance(balance)
    print("Bye")
    exit()


def round_to_two_decimals(number):
    return round(number, 2)


def is_non_positive_number(number):
    if number <= 0:
        print("The amount must be positive.")
        return True
    return False


def main():
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
