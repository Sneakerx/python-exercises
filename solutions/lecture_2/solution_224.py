"""Check Membership in a Set"""


def is_in_set(value, set):
    return value in set


digits = {0, 1, 2, 3, 4, 5}
print(is_in_set(1, digits))  # Output: True
print(is_in_set(7, digits))  # Output: False
