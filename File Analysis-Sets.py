#Mallory Milstead
#3/27/2018
#CSC-121
#This program accepts two files as sets and compares the text within them.


#Create an empty set.
file1 = set()

#Create an empty string.
data = ""

#Open file.
openOne = open("first_file.txt", "r")

#For each line in the file, read it into "data" variable, strip the period
#split it by spaces and then "update" the empty set with those values.
for line in openOne:
    data +=line
    data = data.strip('.')
    split1 = data.split(" ")
    file1.update(split1)
print(data + '\n')


#Create an empty set.
file2 = set()

#Create an empty string.
data2 = ""

#For each line in the file, read it into "data2" variable, strip the period
#split it by spaces and then "update" the empty set with those values.
openTwo = open("second_file.txt", "r")
for line in openTwo:
    data2 += line
    data2 = data2.strip('.')
    #If a comma appears in any of the lines, reaplace it with nothing ("").
    for char in line:
        if char in ",":
            data2 = data2.replace(char,"")
    split2 = data2.split(" ")
    file2.update(split2)
print(data2 + '\n')

#print(file1)

#print(file2)

#Print all of the values in both of the sets (Union)
union = set()
union = file1 | file2

print("1. These are the values of the two sets." + '\n')
print (union)
print ('\n')



#Print the words that are found in both sets (Intersection)
intersect = set()
intersect = file1 & file2

print ("2. These are the values that are shared by the sets." + '\n' )
print(intersect)
print ('\n')

#Print the words that appear in the first list but not in the second (Difference).
file1diff = set()
file1diff = file1 - file2

print("3. These are the values that are in the first set, but not the second."+ '\n')
print (file1diff)
print ('\n')

#Print the words that appear in the first list but not in the second (Difference).
file2diff = set()
file2diff = file2 - file1

print("4. These are the values that are in the second set, but not the first."+ '\n')
print (file2diff)
print ('\n')

#Print the words that are unique to both files (Symmetric Difference)
unique = set()
unique = file1 ^ file2
    
print("5. These are the values that are not shared by the sets."+ '\n')
print (unique)
print ('\n')








    
