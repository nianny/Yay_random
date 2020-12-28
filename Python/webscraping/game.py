import re
import random
import os.path
import scrape

message = """
Hallo and welcome to the first game created ever by me.
This is a hangman game created in the form of a webscrape!!!
The words are derived from enchantedlearning.com/wordlist/ 
and good luck for the game :)

Please remember to run the code from the directory all the
code you downloaded are in. Thank you.

"""
print(message)
if not os.path.isfile('hallo.txt'):
    scrape.scrape()
words = []
with open ('hallo.txt', 'r') as t:
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
