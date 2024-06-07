# ------------------------------------------------------------------------------------------ #
# Title: assignment08_presentation_classes
# Desc: Collection of presentation classes for employee rating application
# Change Log:
#   aliciad, 06/04/2024, Created script
# ------------------------------------------------------------------------------------------ #

from data_classes import Employee


class IO:
    """
    A collection of presentation layer functions to manage user input and output

    Change Log:
        aliciad, 06/04/2023, Created class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays standardized error messages for application to user

        Args:
            message: string with message data
            error: Exception object with technical message

        Return:
            none

        Change Log:
            aliciad, 06/04/2024, Created function
        """

        print(message, end="\n\n")
        if error is not None:
            print("--- Error Details ---")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """
        Displays application menu choices to user

        Args:
            menu: string displaying menu choices

        Return:
            none

        Change Log:
            aliciad, 06/04/2024, Created function
        """

        print(menu, end="\n\n")

    @staticmethod
    def input_menu_choice():
        """
        Processes user's menu choice

        Args:
            none

        Return:
            choice: string with user's choice

        Change Log:
            aliciad, 06/04/2024, Created function
        """

        choice = "0"
        try:
            choice = input("Choose a menu option (1-4): ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Invalid option.  Please choose between 1-4.")
        except Exception as error_message:
            IO.output_error_messages("\n", error_message)
        return choice

    @staticmethod
    def input_employee_data(employee_data: list):
        """
        Processes user's input for first name, last name, review date and review rating.

        Args:
            employee_data: list of dictionary rows

        Return:
            list

        Change Log:
            aliciad, 06/04/2024, Created function
        """
        try:
            employee_first_name = input("Enter the employee's first name: ")
            employee_last_name = input("Enter the employee's last name: ")
            review_date = input("Enter the date of employee review: ")
            review_rating = int(input("Enter the employee's rating (1-5): "))

            new_employee_rating = Employee(
                employee_first_name, employee_last_name, review_date, review_rating
            )

            employee_data.append(new_employee_rating)
            print()
            print(
                f"You have logged a review for {employee_first_name} {employee_last_name}"
                f" of {review_rating} on {review_date}."
            )
        except ValueError as error_message:
            IO.output_error_messages(
                "\nInvalid Entry.  See details below.", error_message
            )
        except Exception as error_message:
            IO.output_error_messages(
                "\nUnknown Error.  Please contact support.", error_message
            )
        return employee_data

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Output current employee data to user

        Args:
            employee_data: list of employee object data

        Return:
            none

        Change Log:
            aliciad, 06/04/2024, Created function
        """

        print("-" * 50)
        print("The current data is: ")
        for employee in employee_data:
            print(
                employee.employee_first_name,
                employee.employee_last_name,
                employee.review_date,
                employee.review_rating,
            )
        print("-" * 50, end="\n\n")
