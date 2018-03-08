"""Mallory Milstead
    2/22/2018
    CSC-121-0001
    This program takes input from a file as a list and performs calculations"""


def main():

    #Assign variable to function to hold list of values.
    numList = getNums()

    #Call getMin function while passing numList variable.
    getMin(numList)

    #Call getMax function while passing numList variable.
    getMax(numList)

    #Assign variable to getSum to hold the total of the values.
    total = getSum(numList)

    #Call getAvg function while passing the total variable.
    getAvg(total, numList)

def getNums():

    #Open file.
    infile = open('numbers.txt', 'r')

    #Read each line in the file and assign it to a list variable.
    inputValues = infile.readlines()
    
    #Close the file.
    infile.close()
    

    #Initiate variable.
    index = 0

    #While the index is less that the number of values, strip the newline.
    while index < len(inputValues):
        inputValues[index] = inputValues[index].rstrip('\n')
        index +=1
        
        
    #Return inputValues to getNums function.
    return inputValues


def getMin(numList):

    #Assign variable to minimum function.
    lowest = min(numList)

    #Print statement.
    print ("The lowest number in the list is ", lowest)

    

def getMax(numList):

    #Assign variable to maximum.
    largest = max(numList)

    #Print statement.
    print ("The largest number in the list is ", largest)
    

def getSum(numList):

    #Initialize variable.
    total = 0

    #Create for loop that accumulates the values in numList.
    for each in numList:
        total += int(each)

    #Print statement.
    print ("The sum of the numbers is", total)

    #Return the value of total to the getSum function.
    return total

def getAvg(total, numList):

    #Calcualte average and store value in variable.
    average = total/len(numList)

    #Print statement.
    print ("The average of the numbers is ", average)
    
        

#Call main function.
if __name__ == "__main__":
    main()






        
