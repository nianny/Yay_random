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


"""
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
lives = 9
# print(index)
# print(words[index])
print(f"Just as a clue, the topic of the word is: {topic}")
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
    print(f"Your have {lives} lives left.")
    choice = str(input("Please type in a new character: "))
    if choice not in word:
        lives -= 1
        if (lives<=0):
            print("Awwww. All your lives were lost. Please play again later")
            break
        print("This letter is unfortunately not in the word. Please try again.")
        continue
    
    print("Wow. This letter is indeed in the word. ")
    for i in range(word_length):
        if word[i] == choice:
            alpha[i] = True
