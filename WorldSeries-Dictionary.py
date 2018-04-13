"""Mallory Milstead
    4/9/2018
    CSC-121
    This program opens a file, creates a dictionary from the data and creates
    another dictionary from the first dictionary. It accepts user input and
    generates output for the user from the dictionaries"""


#Defines the main function.
def main():
    years = getYears()
    names = getNames()
    dictionary_year = getDict(years, names)
    year_input = calculate(dictionary_year)
    setOfnames(names, dictionary_year, year_input)
    
    

#This function associates each line in the file with a corresponding year and
#adds that year to a list containing all of the years.
def getYears():
    inFile = open('WorldSeriesWinners.txt', 'r')
    year = 1902
    years = []
    for line in inFile:
        year +=1
        years.append(year)

    #print(years)
    return years

#This function creates a list containing all of the lines(names of teams) in
#the file.
def getNames():

    inFile = open('WorldSeriesWinners.txt', 'r')
    line = ""
    nameWins = []
    for line in inFile:
        line = line.rstrip('\n')
        nameWins.append(line)

    #print (nameWins)
    return nameWins

    
#This function creates a dictionary using the years list as the key and the
#names list as the corresponding values.
def getDict(years, names):

    dictionary = dict(zip(years, names))
    #print (dictionary)
    return dictionary
                      

#This function gets user input as the key and prints the associated value.
def calculate(dictionary_year):

    #print(dictionary_year)
    year_input = int(input('Enter a year in the range 1903-2009: '))

    if year_input == 1904 or year_input == 1994:
        print('The World Series was not played that year.')

    else:
    
        print('In ' + str(year_input)+', the ' + (dictionary_year[year_input]) + ' won the World Series.')
    return year_input


#This function creates a second dictionary from counting the values of the first
# dictionary 
def setOfnames(names, dictionary_year, year_input):

    
    winsList = []
        
    for key in dictionary_year:
        wins = names.count(dictionary_year[key])
        winsList.append(wins)
    
    
    dictionary_wins = dict(zip(names, winsList))
    #print (dictionary_wins)

    if(dictionary_year[year_input]) in dictionary_wins.keys() and year_input != 1904 and year_input != 1994:
        
        print ('They won ' + str(dictionary_wins.get(dictionary_year[year_input])) + ' total World Series.')
        





if __name__ == "__main__":

    main()



    

