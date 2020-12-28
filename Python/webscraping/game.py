import re
import random
import os.path
import scrape

message = """
Hallo and welcome to the first game created ever by me.
This is a hangman game created in the form of a webscrape!!!
The words are derived from enchantedlearning.com/wordlist/ 
and good luck for the game :)

"""
print(message)
if not os.path.isfile('hallo.txt'):
    scrape.scrape()

with open ('hallo.txt', 'r') as t:
    print(t.readline())
