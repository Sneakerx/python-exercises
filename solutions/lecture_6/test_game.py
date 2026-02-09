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

    # Test that the game exits immediately when the user selects "Q".
    #
    # We patch `builtins.input` so that whenever the program calls
    # `input()` it receives the string "Q". We also patch
    # `sys.stdout` with a `StringIO` object so we can capture anything
    # the program prints and assert against it.
    def test_main_quit_game_immediately(self):
        with patch("builtins.input", return_value="Q"), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_stdout:
            # Run the main function; capture its return value so we can
            # assert the program actually finished (returned) instead
            # of looping forever.
            result = game.main()

            # `mock_stdout.getvalue()` contains everything printed to
            # stdout during the call. We expect the welcome text and
            # the goodbye text concatenated.
            self.assertEqual(mock_stdout.getvalue(), self.WELCOME + self.EXIT)

            # The function should return (commonly `None`), which
            # indicates it exited cleanly instead of running forever.
            self.assertIsNone(result)

    # Test that the game handles an invalid input followed by quitting.
    # We simulate the user first entering "invalid" and then "Q" to quit.
    def test_main_invalid_input_then_quit(self):
        with patch("builtins.input", side_effect=["invalid", "Q"]), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_stdout:
            result = game.main()

            # We expect the welcome text, followed by the invalid option
            # message, and then the goodbye message.
            expected_output = self.WELCOME + self.INVALID + self.EXIT
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            self.assertIsNone(result)

    # Test that the game handles the "Create new pokemon" option and then quits.
    # Since `create_new_pokemon()` is a dummy function that loops forever,
    # we mock it to return immediately so the test doesn't hang.
    def test_main_create_then_quit(self):
        with patch("builtins.input", side_effect=["1", "Q"]), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_stdout, patch(
            "game.create_new_pokemon", return_value="Pikachu"
        ) as mock_create:
            result = game.main()

            # We expect the welcome text, followed by the create message,
            # and then the goodbye message. We also expect that the create
            # function was called once.
            expected_output = self.WELCOME + self.CREATE + self.EXIT
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            mock_create.assert_called_once()
            self.assertIsNone(result)

    # Test that the game handles the "Attack a pokemon" option and then quits.
    # Similar to the previous test, we mock `attack_pokemon()` to avoid hanging.
    def test_main_attack_then_quit(self):
        with patch("builtins.input", side_effect=["2", "Q"]), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_stdout, patch(
            "game.attack_pokemon", return_value=None
        ) as mock_attack:
            result = game.main()

            # We expect the welcome text, followed by the attack message,
            # and then the goodbye message. We also expect that the attack
            # function was called once.
            expected_output = self.WELCOME + self.ATTACK + self.EXIT
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            mock_attack.assert_called_once()
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
