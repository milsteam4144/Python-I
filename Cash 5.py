"""This program uses the csv module to read and interpret a Carolina Cash 5
.csv file. The program determines the number of times a number had been drawn
over the course of the game, displays that total. Then it lists the lotto numbers
(1-41) from ascending to descending depending on how many times they've been
drawn."""

import csv
import operator

#Declare columns as keys with empty lists.
def getNums():
    d = {}
    d['date'] = []
    d['num1'] = []
    d['num2'] = []
    d['num3'] = []
    d['num4'] = []
    d['num5'] = []

    #Create a csv reader object.
    dictReader = csv.DictReader(open('NCELCash5.csv', 'r'), fieldnames = ['date', 'num1', 'num2', 'num3', 'num4', 'num5'], delimiter = ',', quotechar = '"')

    #For each row in the csv,
    for row in dictReader:
        #The key is the fieldname and you are appending each item that is separated by a comma.
        for key in row:
            d[key].append(row[key])
    #Add all of the lists to get a list of all of the numbers.
    allnums = (d['num1'] + d['num2'] + d['num3'] + d['num4'] + d['num5'])
    
    #Create a range to iterate through the Cash 5 number pool (1-41)
    _range = range(1,42)
    #Create an empty list to hold the count values of the Cash 5 numbers (1-41)
    _list = []

    #For each number in the range, count the number of times that number occurs and append it to the list.
    for num in _range:
        _list.append(allnums.count(str(num)))
    #print (_list)
        
        
    #Create a new dictionary that uses the range(1-41) as the key and the corresponding value of it's occurances as the values.
        #Dictionaries cannot be sorted, so the code below creates a tuple from the data and sorts it. The default is descending order, so it is
        #Reversed to be in ascending order.
    new_dict = {k: v for k, v in zip(_range, _list)}
    print (new_dict)

    #Create a tuple from the new dictionary that sorts
    sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)
    #print(sorted_dict)

    for item in sorted_dict:
        print (item)
        

        
    #The number (num) appears (count) times as the first number in all of the sets.
##        print (str(num) + ":" + str(d['num1'].count(str(num))))
##        print (str(num) + ":" + str(d['num2'].count(str(num))))
##        print (str(num) + ":" + str(d['num3'].count(str(num))))
##        print (str(num) + ":" + str(d['num4'].count(str(num))))
##        print (str(num) + ":" + str(d['num5'].count(str(num))))

    

        


    
    

def main():

    getNums()

main()
