"""Mallory Milstead
   4/42/2018
   CSC-121
   This is a class called employee that will be used to create employee
   objects with 3 attributes."""

#Create the class.
class Employee:
    #Initialize the attributes with the __init__ method.
    def __init__(self, name, number, department, jobTitle):
        self.__name = name
        self.__id_num = number
        self.__dept = department
        self.__job_title = jobTitle

    #The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    #The set_id_num method sets the id_num attribute.
    def set_id_num(self, number):
        self.__id_num = number

    #The set_dept method sets the dept attribute.
    def set_dept(self, department):
        self.__dept = department

    #The set_job_title method sets the job_title attribute.
    def set_job_title(self, jobTitle):
        self.__job_title = jobTitle

    #The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    #The get_id_num method returns the id_num attribute.
    def get_id_num(self):
        return self.__id_num

    #The get_dept method returns the dept attribute.
    def get_dept(self):
        return self.__dept

    #The get_job_title method returns the job_title attribute.
    def get_job_title(self):
        return self.__job_title

    #The __str__ method returns the object's state as a string.
    def __str__(self):
        return self.__name + "\t" + self.__id_num + "\t" + self.__dept + \
               "\t" + self.__job_title
