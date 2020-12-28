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

Please remember to run the code from the directory all the
code you downloaded are in. Thank you.

"""
print(message)
if not os.path.isfile(f'{directory}\words.txt'):
    scrape.scrape()
words = []
with open (f'{directory}\words.txt', 'r') as t:
    string = t.readline()
    words.append(string.split(','))
    words.append(list(t.readline()))

found = False
index = random.randint(0,len(words)-1)
topic = words[index][0]
word = words[index][1]
word_length = len(word)
lives = 5
print(index)
print(words[index])
print(topic)
print(word)
print(word_length)
# while not found:

#     choice = str(input("Please type in a new character: "))
