"""Mallory Milstead
    CSC-121-0001
    3/8/2018
    This program takes input from file "tdsc01.txt" and formats/manipulates
    the text to create user e-mail addresses"""


def readfile():

    #Open the file.
    infile = open('tdsc01.txt', 'r')

    #Read each line in the file and assign it to a list variable.
    data = infile.readlines()


    #Convert each item in the list to a string.
    index = 0
    while index < len(data):
        data[index] = str(data[index])
        index +=1

    #Return the values in data to the function as variable myList.
    return data

def createEmails(text):

    #Create file to write new data to.
    outfile = open('User E-mail Addresses.txt', 'w')

    #Create header for columns.
    header = ("First Last" + '\t'*4 + "Student E-mail")

    #Write header to file.
    outfile.write(header+ '\n' + '\n')
    print(header)
    

    for line in text:

        #Determine fields to format for first & last names.
        name = line[13:33]
        name = name.rstrip()
        name = name.split( )
        
        #Format first name.
        firstname = name[1]
        firstInitial = firstname[0]
        #print (firstname)
        
        #Format last name.
        lastname = name[0]
        lastname = lastname.rstrip(",")
        last7 = lastname[:7]
        #print (lastname)

        #Determine fields to format for studentID number.
        iD = line[76:80]
        #print (iD)

        #Create variable for email domain.
        domain = "@student.faytechcc.edu"

        #Concatenate the fields to create username.
        firstlast = firstname + " " + lastname
        email = last7 + firstInitial + iD + domain + '\n'
        print(firstlast + '\t'*3 + email)

        #For each line, write the data to the new file.
        outfile.writelines(firstlast + '\t'*3 + email)

def main():
    myList = readfile()
    new = createEmails(myList)

#Call main function.
if __name__ == "__main__":
    main()
