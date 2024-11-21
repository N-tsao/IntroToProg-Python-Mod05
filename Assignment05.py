import json #file needs to import json before starting program
# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Nicole Tsao,11/19/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: dict = {}  # Holds combined JSON data.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try: #will execute the first block of code underneath
    file = open(FILE_NAME, "r") #opens json file
    students = json.load(file) #loads json file/ data stored in file
    file.close() #saves file
except FileNotFoundError as e: #block of code will execute if try fails, and file is not available
    print("Text file must exist before running this script!\n")
    print("--Technical Error Message")
    print(e,e.__doc__, type(e), sep='\n')
except Exception as e: #exception error that will also execute if try block fails
    print("There was a non-specific error\n")
    print("--Technical error--")
    print(e, e.__doc__, type(e), sep='\n')
finally: #the block under finally will execute regardless of try and except
    if file is not None and not file.closed: #used this line of code since file.closed == False
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): #makes sure ALL characters in string are alphabetic
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): #makes sure ALL characters in string are alphabetic
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            if not course_name.isalnum(): #makes sure ALL characters in string are either alphabetic or numeric
                raise ValueError("Course name must be alphanumeric.")
            student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e: #this block of code will execute along with raise ValueError if try block fails
            print(e)
            print("--Technical Error found--")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e: #this block of code will execute along with raise ValueError if try block fails
            print("There was a non-specific error")
            print("--Technical Error Message")
            print(e, e.__doc__, type(e), sep="\n")
            continue
    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try: #this will execute the code below first
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            continue
        except TypeError as e: #if there is an error with the block of code above, this will execute
            print("Please check that the data is a valid JSON format\n")
            print("--Technical error message--")
            print(e.__doc__, type(e), sep="/n")
        except Exception as e: #if try block does not execute then the except blocks will execute
            print("--Technical error message--")
            print("Built in python error info: ")
            print(e.__doc__, type(e), sep="\n")
        finally: #finally block will execute regardless of try and except
            if file is not None and not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
