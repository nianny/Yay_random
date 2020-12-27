from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

url2 = "https://www.enchantedlearning.com/wordlist/adjectives.shtml"
page2 = urlopen(url2)
html2 = page2.read().decode("utf-8")
soup2 = BeautifulSoup(html2, "html.parser")

adjectives = []
for i in soup2.find_all("div",  {"class": "wordlist-item"}):
    string = str(i)[27:-6]
    adjectives.append(string)

length = len(adjectives)
print(adjectives[random.randint(0,length-1)])


    


