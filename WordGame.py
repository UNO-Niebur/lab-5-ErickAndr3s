#WordGame.py
#Erick Andres
#Date: 02/22/2026
#Assignment: Lab 5
#Purpose: To pratice loops, conditionals, and string manipulation by creating a 5 letter word guessing game.


#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter == ch:
            return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return letter == word[spot]

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""
    
    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot):
            feedback += myLetter.upper() #correct letter in location
        elif inWord(myLetter, word ):
            feedback += myLetter.lower()#letter is in word, not correct spot
        else: 
            feedback += "*" #Letter not in word

    return feedback   

def main():
    #Pick a random word from the list of all words
    with open("words.txt", 'r') as wordFile:
        content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList).lower()

    #Ask user for their guess
    guessNum = 1 
    while guessNum <= 6:
        guess = input(f"Guess {guessNum}/6: ").lower()

        #Check if the guess is valid
        while guess not in wordList:
            print("Word not in list.")
            guess = input ("Enter a valid 5 letter word: ").lower()

        #Give feedback using on their word:
        feedback = rateGuess(guess, todayWord)
        print(feedback)

        #Check if guessed the word correctly
        if guess == todayWord:
            print(f"You got it in {guessNum} tries!")
            break

        guessNum += 1
    else:
        print(f"Sorry, the word was '{todayWord}'.")


if __name__ == '__main__':
  main()
