""" Mallory Milstead
   CSC-121-0001
   2/28/2018
   This program opens a file "tdsc01.txt", manipulates/formats the data and
   saves it to a new file."""

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



def modifyStrings(list_name):

    #Create new file to write to.
    outfile = open('Formatted Report.txt', 'w')

    #Create varible to hold the headings text.
    headers = ('ItemID' + '\t' + ' Buyer' + '\t'*3 +
    'Item Name' + '\t' + 'Price' + '\n' + '\n')

    #Write the headers to the outfile.
    outfile.write(headers)

    #For each line in the file, slice the list appropriately and assign that string to a variable.
    #Add formatting as needed.
    for line in list_name:
        itemID = line[7:10] + "-" + line[9:13] + " "
        buyer = line[13:33].ljust(16) + '\t'
        itemName = line[33:48] + " "
        price = '$' + line[75:78] + "." + line[78:]
    
        #Combine all variables to create the new data.
        new_file = itemID + buyer + itemName + price
        print(new_file)
        
        #For each line in the file, write that line to the new file.
        outfile.writelines(new_file)

    #Initialize variable to hold total.
    total = 0
    #For loop reads each line in the file.
    for line in list_name:
        #Convert the string to a float and assign it to "price" variable.
        price = float(line[75:78] + "." + line[78:])
        #Create accumulator.
        total +=price

    #Convert total back to a string, add the "$" and print.
    total_string = ('\n' + '\n' + "The total of the prices is "+ str('${:,.2f}'.format(total))+ '\n')

    #Write the line to the file.

    outfile.write(total_string)

    #Calculate average using total and length of myList (original data)
    average = total / (len(list_name))
    avg_string = ('\n' + "The average of the prices is " + '${:,.2f}'.format(average) + '\n')
    #Write the line to the file.
    outfile.write(avg_string)


    #Return the newly formatted data to the function as variable new.
    return new_file



    
def main():
    myList = readfile()
    new = modifyStrings(myList)


#Call main function.
if __name__ == "__main__":
    main()



