# ------------------------------------------------------------------------------------------ #
# Title: assignment08_data_classes
# Desc: Collection of data classes for employee rating application
# Change Log:
#   aliciad, 06/03/2024, Created script
# ------------------------------------------------------------------------------------------ #

from datetime import date


class Person:
    """
    Defines parent class to house employee's first and last name.

    Properties:
        employee_first_name (str): The employee's first name
        employee_last_name (str): The emplpoyee's last name

    Change Log:
        aliciad, 06/03/2024, Created class
    """

    # Initiating objects of the Person class which includes employee's first and last names
    def __init__(self, employee_first_name: str = "", employee_last_name: str = ""):
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name

    # Creates the employee's first name object and returns it as a private variable
    @property
    def employee_first_name(self):
        return self.__employee_first_name.title()

    # Sets the employee's first name as a string and verifies it for valid characters
    @employee_first_name.setter
    def employee_first_name(self, value: str):
        if value.isalpha() and len(value) != 0:
            self.__employee_first_name = value
        else:
            raise ValueError(
                "First name can't contain alphanumeric values or be empty."
            )

    # Creates the employee's last name object and returns it as a private variable
    @property
    def employee_last_name(self):
        return self.__employee_last_name.title()

    # Sets the employee's last name as a string and verifies it for valid characters
    @employee_last_name.setter
    def employee_last_name(self, value: str):
        if value.isalpha() and len(value) != 0:
            self.__employee_last_name = value
        else:
            raise ValueError("Last name can't contain alphanumeric values or be empty.")

    # String represenation returning comma-separated string
    def __str__(self) -> str:
        return f"{self.employee_first_name},{self.employee_last_name}"


class Employee(Person):
    """
    Defines child class of Person and adds review date and review rating.

    Properties:
        employee_first_name (str): The employee's first name
        employee_last_name (str): The emplpoyee's last name
        review_date (date): The date of the employee's review
        review_rating (int): The review rating of the employee's performance (1-5)

    Change Log:
        alicia, 06/03/2024, Created class
    """

    # Initiating objects of the Employee class which inherits employee's names
    # from the Person class and adds review date and review rating
    def __init__(
        self,
        employee_first_name: str = "",
        employee_last_name: str = "",
        review_date: str = "1900-01-01",
        review_rating: int = 3,
    ):
        super().__init__(
            employee_first_name=employee_first_name,
            employee_last_name=employee_last_name,
        )
        self.review_date = review_date
        self.review_rating = review_rating

    # Creates the review date object and returns it as a private variable
    @property
    def review_date(self):
        return self.__review_date

    # Sets the review date as a string and verifies it for the correct format
    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except:
            raise ValueError("Invalid date format.  Must be YYYY-MM-DD.")

    # Creates the review rating object and returns it as a private variable
    @property
    def review_rating(self):
        return self.__review_rating

    # Sets the review rating as an integer and verifies it for the correct value
    @review_rating.setter
    def review_rating(self, value: int):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Invalid entry.  Please choose values 1 - 5.")

    # Redefining string representation as comma-separated string
    def __str__(self) -> str:
        return f"{self.employee_first_name},{self.employee_last_name}, \
        {self.review_date},{self.review_rating}"
