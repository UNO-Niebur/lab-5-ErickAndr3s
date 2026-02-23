#CaesarCypher.py
#Name: Erick Andres
#Date: 02/22/2026
#Assignment: Lab 5
#Purpose: To practice working with strings, loops and logic by creating a program that encrypts and decrypts messages using a Caesar Cipher.

#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

#def decode(message, key):
    #We will want to decode the message here.
def decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper() 
    plaintext = ""

    for letter in message:
        if alpha.find(letter) >= 0:
            spot = (alpha.find(letter) -key) % 26
            plaintext = plaintext + alpha[spot]
        else:
            plaintext = plaintext + letter
    return plaintext 


def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)

    #plaintext = decode(secret, key)

    plaintext = decode(secret, key)
    print("Decrypted:", plaintext)
    #print ("Decrypted:", plaintext)


if __name__ == '__main__':
  main()
