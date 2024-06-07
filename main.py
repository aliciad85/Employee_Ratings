# ------------------------------------------------------------------------------------------ #
# Title: assignment08_main
# Desc: The main execution block for the employee rating application
# Change Log:
#   aliciad, 06/04/2024, Created script
# ------------------------------------------------------------------------------------------ #

from sys import exit
from presentation_classes import IO
from processing_classes import FileProcessor

FILE_NAME: str = "employee_rating.json"
MENU: str = """
----- Employee Ratings Application -----
    Select from the following menu:
     1. Enter new employee rating
     2. Show current data
     3. Save data to file
     4. Exit the program
----------------------------------------
"""

employees: list = []
menu_choice = ""

if __name__ == "__main__":
    employees = FileProcessor.read_employee_data_from_file(
        file_name=FILE_NAME, employee_data=employees
    )

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()
        match menu_choice:
            case "1":
                IO.input_employee_data(employee_data=employees)

            case "2":
                IO.output_employee_data(employee_data=employees)

            case "3":
                FileProcessor.write_employee_data_to_file(
                    file_name=FILE_NAME, employee_data=employees
                )
                print("INFO: New ratings have been saved.")

            case "4":
                print("Program Ended.")
                exit()
