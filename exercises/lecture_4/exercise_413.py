"""Create method get_info that returns the value of a specific attribute."""


class Account:
    def __init__(self, owner, account_number, initial_balance):
        self._owner = owner
        self._account_number = account_number
        self._initial_balance = initial_balance

    def get_info(self, key):
        pass  # TODO: Implement this method


my_account = Account("Jon Schnee", 333, 1000.0)
print(my_account.get_info("owner"))
print(my_account.get_info("account_number"))
print(my_account.get_info("initial_balance"))
