"""Prints all kinds of parameters."""


def print_param(param1, param2, *args, **kwargs):
    """print all kinds of parameters."""
    print("Positional Arguments:")
    print(f"param1: {param1}")
    print(f"param2: {param2}")
    print("\nNon-Positional Arguments:")
    for index, value in enumerate(args):
        print(f"{index}: {value}")

    print("\nNon-Positional Keyword Arguments:")
    for key, value in zip(list(kwargs.keys()), list(kwargs.values())):
        print(f"Key: {key}, Value: {value}")


print_param(5, 6, "Noah", "Klaus", "Gerda", speed=5, strength=5, height=80)
