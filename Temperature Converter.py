# Program prompts user to input a conversion method and temp, then converts it.
# 1/29/2018
# CSC-121-0001
# Mallory Milstead


def main():
    again = 'y'
    while again == "yes" or again == "Yes" or again =="y":
        mainMenu()
        getInput()
        print(' ')
        again = input("Would you like to run the program again? ")
    while again != "yes" or again != "Yes" or again != 'y':
        print ("Goodbye")
        break
    
   

def mainMenu():
    print(' ')
    print('This program will convert temperatures between Fahrenheit and Celcius')
    print(' ')
    print ('To convert Celcius to Fahrenheit, Enter 1')
    print ('To convert Fahrenheit to Celcius, Enter 2')

def getInput():
    menuChoice = input('Enter 1 or 2 to convert: ')
    if menuChoice == "1" :
        toFahrenheit()
    elif menuChoice == "2":
        toCelsius()
    else:
        print('User entered an incorrect value')
        return menuChoice
    
    
def toFahrenheit():
    temp = int(input('What is the temperature you would like to convert? '))
    convertTof = (temp * 1.8) + 32
    print(temp, "Celsius is equal to", convertTof, "Fahrenheit.")

def toCelsius():
    temp = int(input('What is the temperature you would like to convert? '))
    convertToC = (temp - 32) * .5556
    print(temp, "Fahrenheit is equal to", convertToC, "Celsius.")

main()




    
