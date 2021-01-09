import re
import random
import os.path
import scrape
from pathlib import Path
directory = Path(__file__).parent.absolute()


message = """
Hallo and welcome to the first game created ever by me.
This is a hangman game created in the form of a webscrape!!!
The words are derived from enchantedlearning.com/wordlist/ 
and good luck for the game :)

Please raise any possible issues on github
Also, avoid moving the files game.py and scrape.py to seperate directories. Thank you!!!
"""



"""
How does this thing work???
If you did not play this before/did not download the words together, it will import scrape.py,
which will run a webscrape and save all the words in a text file that can then be accessed here.

In this code, a random index is come up with (on the list of all words derived from the word text file)
using randint, and the hangman game will then be implemented.
One clue will be given when you are at 6 and 3 lives respectively. However, if the clue given has already
been found, the clue will be voided.
Thank you.

Any possible queries please feel free to raise issues of Github!!!
"""

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




print(message)
if not os.path.isfile(directory.joinpath("words.txt")):
    scrape.scrape()
words = []
with open (directory.joinpath("words.txt"), 'r') as t:
    string = t.readlines()
    for i in string:
        words.append(i.split(','))

found = False
index = random.randint(0,len(words)-1)
topic = words[index][0]
word = words[index][1][:-1]
word_length = len(word)
lives = 7
# print(index)
# print(words[index])
agree = True
while agree:
    agr = input(f"The current topic is {topic}. If you wish to change, input 'c'. Else, input 'n': ")
    if agr == 'c':
        index = random.randint(0,len(words)-1)
        topic = words[index][0]
        word = words[index][1][:-1]
        word_length = len(word)
    elif agr == 'n':
        agree = False
        
# print(word)
# print(word_length)
alpha = []
for i in range(word_length):
    alpha.append(False)
while not found:
    output = ""
    a = True
    for i in range(word_length):
        if not alpha[i]:
            output+="_ "
            a = False
        else:
            output+=word[i]
    
    if a == True:
        found = True
        print("You found it :)")
        print("The word is: "+word)
        break
    print(output)
    print("Lives: " + str(lives)+HANGMANPICS[7-lives])

    choice = str(input("Please type in a new character: "))
    print("Now you know at least 1 letter. Keep trying")
    if choice not in word:
        lives -= 1
        if (lives<=0):
            print("Awwww. All your lives were lost. Please play again later")
            break
        if (lives == 6):
            clue = random.randint(0, word_length-1)
            clue_word = word[clue];
            for i in range(word_length):
                if word[i] == clue_word:
                    alpha[i] = True
            
        if (lives == 3):
            clue = random.randint(0, word_length-1)
            clue_word = word[clue];
            for i in range(word_length):
                if word[i] == clue_word:
                    alpha[i] = True
        print("This letter is unfortunately not in the word. Please try again.")
        print('\n')
        continue
    
    print("Wow. This letter is indeed in the word. ")
    print('\n')
    for i in range(word_length):
        if word[i] == choice:
            alpha[i] = True
