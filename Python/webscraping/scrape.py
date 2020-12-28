from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import os.path
from pathlib import Path
directory = Path(__file__).parent.absolute()

def scrape ():
    url = "https://www.enchantedlearning.com/wordlist/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")


    message = """
Because this is currently your first time playing this game,
or you have changed the directory of the files, you will have
to wait for around 10 minutes while waiting for the words
to be etracted. Please be patient.

"""
    print(message)
    print("Accessing main page")

    links = []
    for link in soup.find_all("a", target="_top"):
        if (str(link.get('href'))[:10]=="/wordlist/"):
            #print(link.get('href'))
            links.append([str(link.get('href')), link.text])
            #print(link.get('href'))
    links = links[:-3]

    print("Accessing various directories")

    word = []
    for i in range(len(links)):
        url2 = "http://www.enchantedlearning.com"+links[i][0]

        page2 = urlopen(url2)
        html2 = page2.read().decode("utf-8")
        soup2 = BeautifulSoup(html2, "html.parser")
        words = []
        for i in soup2.find_all("div",  {"class": "wordlist-item"}):
            string3 = i.text 
            words.append(string3)
            
        word.append(words)




    # out = random.randint(0,len(word))
    # inside = random.randint(0,len(word[out]))

    print("Saving data")
    with open (directory.joinpath("words.txt"), 'w') as t:
        for i in range (len(word)):
            for p in range (len(word[i])):
                if ' ' not in word[i][p]:
                    t.write(str(links[i][1]))
                    t.write(',')
                    t.write(str(word[i][p]))
                    t.write('\n')
    
    print("Data saved")

    # print(f"The topic is about: {links[out][1]}")
    # print(f"Hmm. The word is: {word[out][inside]}")



