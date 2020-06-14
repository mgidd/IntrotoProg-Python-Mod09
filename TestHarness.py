# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A module for testing other modules
# ChangeLog (Who,When,What):
#   MGiddings,6.12.2020,Created script
#   MGiddings,6.12.2020,Added code to test Person class
#   MGiddings,6.12.2020,Added code to test Employee class
#   MGiddings,6.12.2020,Added code to test FileProcessor class
#   MGiddings,6.12.2020,Added code to test EmployeeIO class
# ---------------------------------------------------------- #

from DataClasses import Person, Employee
from ProcessingClasses import FileProcessor
from IOClasses import EmployeeIO

# Test data module - class Person
objP1 = Person("Bob", "Smith")
objP2 = Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test data module - class Employee
objP1 = Employee(1, "Bob", "Smith")
objP2 = Employee(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module - class FileProcessor
FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Employee(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO module - class EmployeeIO
EmployeeIO.print_menu_items()
EmployeeIO.print_current_list_items(lstTable)
print(EmployeeIO.input_employee_data())
print(EmployeeIO.input_menu_options())
