"""Prints the current user's name."""

import os

nutzername = os.getlogin()
print(f"Hallo {nutzername}!")
