# ------------------------------------------------------------------------------------------ #
# Title: assignment08_processing_classes
# Desc: Collection of processing classes for employee rating application
# Change Log:
#   aliciad, 06/04/2024, Created script
# ------------------------------------------------------------------------------------------ #

import json
from data_classes import Employee
from presentation_classes import IO


class FileProcessor:
    """
    Class to handle data storage and retrieval using json files

    Change Log:
        aliciad, 06/04/2024, Created class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list):
        """
        Read file and load to json and return list

        Args:
            file_name: file name as a string
            employee_data: list of employee dictionary rows

        Return:
            list

        Change Log:
            aliciad, 06/04/2024, Created function

        """
        try:
            with open(file_name) as file:
                list_of_dict_data = json.load(file)
                for employee in list_of_dict_data:
                    employee_object: Employee = Employee(
                        employee_first_name=employee["FirstName"],
                        employee_last_name=employee["LastName"],
                        review_date=employee["ReviewDate"],
                        review_rating=employee["ReviewRating"],
                    )
                    employee_data.append(employee_object)
        except FileNotFoundError as error_message:
            IO.output_error_messages("\nFile not found.", error_message)
        except Exception as error_message:
            IO.output_error_messages(
                "\nUnknonw Error.  Please contact support.", error_message
            )
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Write data to json file

        Args:
            file_name: file name as a string
            employee_data: list of employee dictionary rows

        Return:
            none

        Change Log:
            aliciad, 06/04/2024, Created function
        """
        try:
            list_of_dict_data: list = []
            for employee in employee_data:
                employee_json: dict = {
                    "FirstName": employee.employee_first_name,
                    "LastName": employee.employee_last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating,
                }
                list_of_dict_data.append(employee_json)
            with open(file_name, "w") as file:
                json.dump(list_of_dict_data, file)
        except FileNotFoundError as error_message:
            IO.output_error_messages("\nFile not found.", error_message)
        except Exception as error_message:
            IO.output_error_messages(
                "\nUnknown Error.  Please contact support.", error_message
            )
