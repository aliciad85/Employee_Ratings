# ------------------------------------------------------------------------------------------ #
# Title: assignment08_test_data_classes
# Desc: Collection of unit tests for data classes for employee rating application
# Change Log:
#   aliciad, 06/03/2024, Created script
# ------------------------------------------------------------------------------------------ #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    """
    Defines test class for unit testing the Person class.

    Properties:
        employee_first_name (str): The employee's first name
        employee_last_name (str): The emplpoyee's last name

    Change Log:
        aliciad, 06/03/2024, Created class
    """

    # Testing init method of Person class
    def test_person_init(self):
        test_person = Person("John", "Doe")
        self.assertEqual(test_person.employee_first_name, "John")
        self.assertEqual(test_person.employee_last_name, "Doe")

    # Testing error handling for invalid inputs
    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            Person("123", "Doe")
        with self.assertRaises(ValueError):
            Person("John", "123")
        with self.assertRaises(ValueError):
            Person("", "Doe")
        with self.assertRaises(ValueError):
            Person("John", "")

    # Testing Person data string representation
    def test_person_str(self):
        test_person = Person("John", "Doe")
        string_representation = str(test_person)
        expected_value = "John,Doe"
        self.assertEqual(string_representation, expected_value)


class TestEmployee(unittest.TestCase):
    """
    Defines test class for unit testing the Employee class.

    Properties:
        employee_first_name (str): The employee's first name
        employee_last_name (str): The emplpoyee's last name
        review_date (date): The date of the employee's review
        review_rating (int): The review rating of the employee's performance (1-5)

    Change Log:
        alicia, 06/03/2024, Created class
    """

    # Testing init method of Employee class
    def test_employee_init(self):
        test_employee = Employee("John", "Doe", "2024-06-03", 4)
        self.assertEqual(test_employee.employee_first_name, "John")
        self.assertEqual(test_employee.employee_last_name, "Doe")
        self.assertEqual(test_employee.review_date, "2024-06-03")
        self.assertEqual(test_employee.review_rating, 4)

    # Testing error handling for invalid review date and rating
    def test_employee_invalid_rating(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "06-03-2024", 4)
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "", 6)
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "2024-06-03", 6)

    # Testing Employee data string represenation
    def test_employee_str(self):
        test_employee = Employee("John", "Doe", "2024-06-03", 4)
        string_representation = str(test_employee)
        expected_value = "John,Doe, \
        2024-06-03,4"
        self.assertEqual(string_representation, expected_value)


if __name__ == "__main__":
    unittest.main()
