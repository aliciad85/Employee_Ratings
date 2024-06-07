# ------------------------------------------------------------------------------------------ #
# Title: assignment08_test_presentation_classes
# Desc: Collection of unit tests for presentation classes for employee rating application
# Change Log:
#   aliciad, 06/04/2024, Created script
# ------------------------------------------------------------------------------------------ #

import unittest
from unittest.mock import patch
from presentation_classes import IO


class TestIO(unittest.TestCase):
    """
    Define test class for unit testing the IO class

    Change Log:
        aliciad, 06/04/2024, Created test class
    """

    def setUp(self):
        self.test_employee_data = []

    def tearDown(self):
        self.test_employee_data = [1, 2, 3, 4]

    # Testing for a valid menu option
    def test_input_menu_choice(self):
        with patch("builtins.input", return_value="2"):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, "2")

    # Testing error handling for an invalid menu option
    def test_invalid_input_menu_choice(self):
        with self.assertRaises(Exception):
            IO.input_menu_choice("5")

    # Testing for user input
    def test_input_employee_data(self):
        with patch("builtins.input", side_effect=("John", "Doe", "2024-06-04", 4)):
            IO.input_employee_data(self.test_employee_data)
            self.assertEqual(len(self.test_employee_data), 1)
            self.assertEqual(self.test_employee_data[0].employee_first_name, "John")
            self.assertEqual(self.test_employee_data[0].employee_last_name, "Doe")
            self.assertEqual(self.test_employee_data[0].review_date, "2024-06-04")
            self.assertEqual(self.test_employee_data[0].review_rating, 4)


if __name__ == "__main__":
    unittest.main()
