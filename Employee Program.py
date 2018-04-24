"""Mallory Milstead
   2/42/2018
   CSC-121
   This program uses an "Employee" class to create three class objects and
   displays the object's data attributes using a list."""

import employee

def main():

    #Calls the make_list function and assigns the returned value to a variable.
    employees = make_list()

    #Display the data in the list.
    print("Here is the data that was entered: ")
    display_list(employees)


#This function gets data from user and then returns a list of objects
#containing the data.
def make_list():

    #Create an empty list.
    emp_list = []

    #Create a variable to control the for loop.
    numToadd = int(input("How many employees will you add? "))
    print()
    print("Enter the data for", numToadd, "employees:")
    print()

    #For a number of times, get data, create object and add to list.
    for count in range(0,numToadd):
        #Get the employee data.
        name = input("Enter the employee's name: ")
        number = input("Enter the employee's ID number: ")
        department = input("Enter the employee's department: ")
        jobTitle = input("Enter the employee's job title: ")
        #Print a blank line for easy reading.
        print()

        #Create a new Employee object and assign it to the employee variable.
        employeeToadd = employee.Employee(name, number, department, jobTitle)

        #Add the object to the list.
        emp_list.append(employeeToadd)

    #Return the list.
    return emp_list

#The display function accepts a list as the argument and displays the data stored
#in each object.
def display_list(someList):
    for item in someList:
        print("Employee Name: " + item.get_name())
        print("ID Number: " + item.get_id_num())
        print("Department: " + item.get_dept())
        print("Job Title: " + item.get_job_title())
        print()

#Call the main funtion.
if __name__ == "__main__":

    main()



    
