#LetterFrequency.py
#Name:Erick Andres
#Date:02/22/2026
#Assignment:Lab 5
#Purpose: To count how often each letter appears in a message and save reults for analysis 


#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    #Initialize frequency list for all letters
    freq = [0]*26

    #loop through each letter
    for letter in message:
        if letter in alpha: #only count letters
            spot = alpha.find(letter)
            freq[spot] += 1 #Increment the frequency


    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.
    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)



if __name__ == '__main__':
  main()
