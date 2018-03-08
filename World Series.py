"""
Mallory Milstead
2/22/2018
CSC-121-0001)
This program reads the contents of a file into a list. The user then inputs
a specific element of the list and the number of times that element exists
in the list is displayed"""

def main():

    #Set a variable to make the program run once.
    again = 'y'

    #While loop runs the program if users specifies y or Y.
    while again == "y" or again == "Y":

        #Assign the openFile function to a variable and runs the function.
        winners = openFile()

        #Runs the countWinner function while passing the value of winner to it.
        countWinner(winners)

        #Prompt user to run the program again?
        print (" ")
        again = str(input("Would you like to search again? Enter 'y' to search."))

    #Ends the program if the user does not enter y or Y.
    while again != "y" or again != "Y":
        print ("Goodbye")
        break

def openFile():

    #Open file WorldSeriesWinners.txt.
    infile = open('WorldSeriesWinners.txt', 'r')

    #Read lines from file into a list.
    #(readlines function returns the items as a list)
    winners = list(infile.readlines())

    #Close the file.
    infile.close()

    #Strip the newline(\n) from each element.
    index = 0
    while index < len(winners):
        winners[index] = winners[index].rstrip('\n')
        index +=1

    return winners


def countWinner(winners):

    print (" ")

    #Prompt user to enter a team name.
    teamName = input("Enter the name of a team to determine how many " +
                         "World Series games they have won:")
    #Initialize a variable to count the number of times an element exists
    #in the list.
    if teamName in winners:
        count = winners.count(teamName)
        #The Boston Red Sox won their first World Series under a different name.
        #This statement adds that win to their total.
        if teamName == "Boston Red Sox":
            count +=1
        print (teamName, "have won", count, "World Series games.")
    else:
        print("That team has not won any World Series games.")





#Runs the main function.
if __name__ == "__main__":

    main()








    
