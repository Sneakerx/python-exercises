"""Unit tests for the game module using i/o patch."""

import unittest
from unittest.mock import patch
from io import StringIO
import game


class TestGame(unittest.TestCase):
    # Predefined expected output fragments used across tests. Keeping
    # these as constants makes assertions clearer and avoids duplication.
    WELCOME = "Welcome to the game\n"
    EXIT = "Bye\n"
    CREATE = "Create Pokemon\n"
    ATTACK = "Attack Pokemon\n"
    INVALID = "Invalid option\n"

    def test_main_quit_game_immediately(self):
        pass

    def test_main_invalid_input_then_quit(self):
        pass

    def test_main_create_then_quit(self):
        pass

    def test_main_attack_then_quit(self):
        pass


if __name__ == "__main__":
    unittest.main()
