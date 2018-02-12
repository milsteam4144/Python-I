# This program reads numbers from a file and
# calculates the average of those numbers. It raises an exception if
# the file can't be opened or the data is not numeric.
# 2/6/2018
# CTI-110 M1HW2 - Exception Handling
# Mallory Milstead


def main():

    try:
        #Open numbers.txt file.
        numFile = open('numbers.txt', 'r')
    

        #Initialize accumulator to zero.
        total = 0.0

        #Initialize a variable to keep count of the numbers.
        count = 0

        #Get numbers from the file.
        for line in numFile:

            #Convert each line to a float.
            number = int(line)

            #Add one to the count for each line read (count + 1 = count).
            count += 1

            #For each line read, add that number to the total.
            total += number

            #Calculate the average.
            average = total/count

        #Print the statement followed by the average.
        print("The average of the numbers is " + str(format(average, ",.2f")))

        #Close the file.
        numFile.close()

    #If the filename cannot be opened or read, raise this exception.
    except IOError:
        print("An error occured trying to read the file.")

    #If the file contains data that is not an integer, raise this exception.
    except ValueError:
        print("Non-numeric data found in the file.")

    

#Call the main function.
main()
