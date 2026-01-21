"""Prints all kinds of utility information."""

import os
import sys
import datetime
import random


def print_login():
    """Prints the current user's name."""
    nutzername = os.getlogin()
    print(f"Hallo {nutzername}!")


def print_version():
    """Prints the current Python version."""
    infos = sys.version
    version = infos.split(" ", maxsplit=1)[0]
    print(version)


def print_time():
    """Prints the current time."""
    time = datetime.datetime.now()
    print(time.strftime("%d.%m.%Y %H:%M:%S"))


def print_random5():
    """Prints 5 random numbers between 1 and 100."""
    values = range(1, 101)
    print(random.sample(values, 5))


def main():
    """Main function to print all utility information."""
    print_login()
    print_version()
    print_time()
    print_random5()


if __name__ == "__main__":
    main()
