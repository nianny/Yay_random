from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

url = "https://www.enchantedlearning.com/wordlist/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

links = [[]]
for link in soup.find_all("a", target="_top"):
    if (str(link.get('href'))[:10]=="/wordlist/"):
        #print(link.get('href'))
        links.append([str(link.get('href')), str(link)])
        print(link.get('href'))
print(len(links))
word = [[]]
for i in range(len(links)):
    url2 = "http://www.enchantedlearning.com"+links[i+1][0]

    page2 = urlopen(url2)
    html2 = page2.read().decode("utf-8")
    soup2 = BeautifulSoup(html2, "html.parser")
    words = []
    for i in soup2.find_all("div",  {"class": "wordlist-item"}):
        string = str(i)[27:-6]
        #print(string)
        words.append(string)
        
    word.append(words)



