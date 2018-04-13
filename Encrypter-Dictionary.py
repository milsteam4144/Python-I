"""Mallory Milstead
   4/12/2018
   CSC-121
   This program opens a file, reads its data and encrypts it using a dictionary.
   Then the program writes the encoded text to a new file. The encrypted file
   is then read and a reverse dictionary is created. The encrypted file is
   decrypted with the reverse dictionary and the output is printed to the screen."""

from tkinter import filedialog
from tkinter import *

#Create tkinter object and then hide the root window.
root = Tk()
root.withdraw()

#Openfiledialog to allow the user to select from only text files...assign that file to variable.
root.filename =  filedialog.askopenfilename(title = "Select file to Encrypt",filetypes = (("text files","*.txt"),("all files","*.*")))
file_to_encrypt = root.filename


#Open the file.
inFile = open(file_to_encrypt, "r")

#Create empty string to initiate variable.
data = ""

#Read data from file into variable.
for line in inFile:
    data += line



#Create dictionary to encode data.
encoder = {"A":">", "B":"C", "C":"B", "D":"E", "E":")", "F":"G", "G":"F", "H":"]", "I":"^", "J":"+", "K":"(",
          "L":"`", "M":"~", "N":"L", "O":"*", "P":"V", "Q":"Z", "R":"!", "S":"X", "T":"Q", "U":"}", "V":"{", "W":"R",
           "X":"5", "Y":"A", "Z":"?", " ":"$", "a":"q", "b":"w", "c":"e", "d":"r", "e":"t", "f":"y", "g":"u", "h":"i",
           "i":"o", "j":"p", "k":"[", "l":"#", "m":"@", "n":"a", "o":"s", "p":"d", "q":"f", "r":"g", "s":"h", "t":"j",
           "u":"k", "v":"l", "w":";", "x":"'", "y":"z", "z":"x", "1":"=", "2":"-", "3":"9", "4":"8", "5":"7", "6":"5",
           "7":"4", "8":"3", "9":"2", "0": "1", ".":"D", ",":"|", '"':"_", ":":"%", "-":"&"}



#Initiate variable with empty string.
encrypted = ""

#For each letter (key), add its value pair to the new variable IF it exists in the dictionary.
for letter in data:
    if letter in encoder:
        encrypted += encoder[letter]
    #If the key is not in the dictionary, keep its original value.
    else:
        encrypted += letter

#Create file and write the encrypted data to it.
outFile = open("ENCRYPTED FILE.txt", "w")
outFile.write(encrypted)
outFile.close()



#Create decoder by switching the key and value positions.

reverseEncoder = dict((value, key) for key, value in encoder.items())

#Prompt user to choose the encrypted file to open.
root.filename =  filedialog.askopenfilename(title = "Select file to Decrypt",filetypes = (("text files","*.txt"),("all files","*.*")))
file_to_decrypt = root.filename


#Open the decrypted file.
inFile = open(file_to_decrypt, "r")

#Initiate new variable to hold the data.
outData = ""

#Assign the data from the file to the variable.
for line in inFile:
    outData += line

decrypted = ""

#For each encrypted character, IF it is found in the reverse dictionary, print its value.
for letter in outData:
    if letter in reverseEncoder:
        decrypted += reverseEncoder[letter]
    else:
        decrypted += letter

#Print the decrypted text.
print(decrypted)





