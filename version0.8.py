#Guess the Word Game
#Zia Mehta
#version0.8
#8/04/16

import random 

def game():
    animalWords = ("tiger", "elephant", "pig", "lion", "shark") # List of words for the computer to pick from
    foodWords = ("chocolate", "dumplings", "rice", "fries", "apples") # List of words for the computer to pick from
    countriesWords = ("spain", "china", "america", "uruguay", "india") # List of words for the computer to pick from
    
    topic = input('Do you want to guess words on animals, food or countries? Type animal, food or countries')
    if topic == 'animal':
        wordGuess(animalWords)
    elif topic == 'food':
        wordGuess(foodWords)
    elif topic == 'countries':
        wordGuess(countriesWords)


def wordGuess(game):
    wordList=game
    word = random.choice(wordList) # Word to be guessed and is picked at random 
    letters_guessed = []
    print ("Guess the Word!")
    print ("You get to give five letters.")
    print ("There are %s letters in the word." % (len(word)))
    guesses = 5
    while guesses != 0: #loop will repeadtedly ask the user for a letter until they run out of turns
        chosenLetter =input("Enter a letter: ")
        if chosenLetter in letters_guessed: #to allow the user to guess different letters each time
            print ("You already guessed that letter.")
        else:
            guesses = guesses - 1
            print ("You have %d guesses left." % (guesses))
            letters_guessed.append(chosenLetter)
    print ("The word:")
    maskedGuess = ""
    for chosenLetter in word:
        if chosenLetter in letters_guessed:
            maskedGuess += chosenLetter
        else: maskedGuess += "-"
    print (maskedGuess)
    finalGuess = input("Guess the word: ")
    finalGuess=finalGuess.lower()
    if finalGuess ==  word:
        print ("Good Job! %s is the word!" % (finalGuess))
    else:
        print ("That is not the word. The word is %s." % (word))      
    
game()
    
    