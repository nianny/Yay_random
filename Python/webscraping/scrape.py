from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import os.path
def scrap ():
    url = "https://www.enchantedlearning.com/wordlist/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")


    message = """
    Hallo people, this is my first time trying out making a hangman game.
    The first time you play might take up to a few minutes to load as it
    will have to download all the words down from the interet.

    I havent figured out how to make the save as txt part, so you have
    to bear with the 10 minutes wait per round in the meantime

    Currently, it outputs a random word with a random topic (after you
    wait for probably 10 minutes. 


    Any errors please raise an issue on github!!!



    """
    print(message)
    print("Accessing main page")

    links = [[]]
    for link in soup.find_all("a", target="_top"):
        if (str(link.get('href'))[:10]=="/wordlist/"):
            #print(link.get('href'))
            links.append([str(link.get('href')), link.text])
            #print(link.get('href'))
    links = links[:-3]

    print("Accessing various directories")

    word = [[]]
    for i in range(len(links)-1):
        url2 = "http://www.enchantedlearning.com"+links[i+1][0]

        page2 = urlopen(url2)
        html2 = page2.read().decode("utf-8")
        soup2 = BeautifulSoup(html2, "html.parser")
        words = []
        for i in soup2.find_all("div",  {"class": "wordlist-item"}):
            string3 = i.text 
            words.append(string3)
            
        word.append(words)




    out = random.randint(0,len(word))
    inside = random.randint(0,len(word[out]))

    with open ('words.txt', 'w') as t:
        for ()

    print(f"The topic is about: {links[out][1]}")
    print(f"Hmm. The word is: {word[out][inside]}")



