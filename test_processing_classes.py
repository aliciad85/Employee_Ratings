# ------------------------------------------------------------------------------------------ #
# Title: assignment08_test_processing_classes
# Desc: Collection of unit tests for processing class for employee rating application
# Change Log:
#   aliciad, 06/04/2024, Created script
# ------------------------------------------------------------------------------------------ #

import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    """
    Class to handle testing data storage and retrieval using json files

    Change Log:
        aliciad, 06/04/2024, Created class
    """

    # Setting up temp file for testing
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.sample_employees = []

    # Clean up and delete the temp file
    def tearDown(self):
        self.temp_file.close()

    def test_read_employee_data_from_file(self):

        # Creating sample data to write to temporary file
        sample_data = [
            {
                "FirstName": "John",
                "LastName": "Doe",
                "ReviewDate": "2024-06-04",
                "ReviewRating": 4,
            },
            {
                "FirstName": "Jane",
                "LastName": "Doe",
                "ReviewDate": "2024-06-04",
                "ReviewRating": 5,
            },
        ]

        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Calling FileProcessor read method to read from temporary file
        # and testing it matches json data
        FileProcessor.read_employee_data_from_file(
            self.temp_file_name, self.sample_employees
        )

        self.assertEqual(len(self.sample_employees), len(sample_data))
        self.assertEqual(self.sample_employees[0].employee_first_name, "John")
        self.assertEqual(self.sample_employees[1].review_rating, 5)

    def test_write_employee_data_to_file(self):

        # Creating sample employee objects for testing
        sample_employees = [
            data.Employee("John", "Doe", "2024-06-04", 4),
            data.Employee("Jane", "Doe", "2024-06-04", 5),
        ]

        # Calling FileProcessor write method to write to temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Reading the data from the temporary file and testing it matches json data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["ReviewRating"], 5)


if __name__ == "__main__":
    unittest.main()
