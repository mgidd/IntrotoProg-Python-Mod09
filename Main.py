# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with modules
# ChangeLog (Who,When,What):
#   RRoot,1.1.2030,Created script
#   RRoot,1.1.2030,Added pseudo-code to start assignment 9
#   MGiddings,6.12,2020,Modified code to complete assignment 9
#   MGiddings,6.13.2020,Modified code for loading data from file
# ------------------------------------------------------------------------ #

# Import modules
from DataClasses import Employee as E
from ProcessingClasses import FileProcessor as FP
from IOClasses import EmployeeIO as eIO

# Declare variables
strFileName = 'EmployeeData.txt'
lstOfEmployeeRows = []

# Main Body of Script  ---------------------------------------------------- #
# Added code to main body to complete assignment 9

# Load data from file into a list of employee objects when script starts
lstFileData = FP.read_data_from_file(strFileName)  # load data from file
for line in lstFileData:
    lstOfEmployeeRows.append(E(line[0], line[1], line[2].strip()))  # add data to list

# Show user a menu of options
while True:
    eIO.print_menu_items()

    # Get user's menu option choice
    strChoice = eIO.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice.strip() == '1':
        eIO.print_current_list_items(lstOfEmployeeRows)

    # Let user add data to the list of employee objects
    elif strChoice.strip() == '2':
        objEmployee = eIO.input_employee_data()
        lstOfEmployeeRows.append(objEmployee)  # add object to list

    # Let user save current data to file
    elif strChoice.strip() == '3':
        FP.save_data_to_file(strFileName, lstOfEmployeeRows)

    # Let user exit program
    elif strChoice.strip() == '4':
        break  # and exit

    else:
        print('Please enter a choice from 1 to 4.')

