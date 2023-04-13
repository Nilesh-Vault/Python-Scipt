# from multiprocessing.sharedctypes import Value
from bs4 import BeautifulSoup as Soup
import requests
import json

# from script.scraper import URL
Bu_facts = {}

URL = "https://www.bu.edu/president/boston-university-facts-stats/"

page = requests.get(URL)
soup = Soup(page.content, 'html.parser')
factsCategories = soup.find(class_ = "facts-categories")

categories = factsCategories.find_all('h5')

facts_list = factsCategories.find_all(class_ = "row list")

for categori , facts in zip(categories, facts_list):
    i = []
    formatCategori = str(categori).replace("<h5>","").replace("</h5>","")

    
    fact = facts.find_all(class_ = 'list-item')
    for j in fact:
        var = []
        var.append(j.find(class_="text").text)
        var.append(j.find(class_="value").text)
        i.append(var)
    Bu_facts[formatCategori] = i


with open('facts.json', 'w') as f:
    json.dump(Bu_facts,f, indent=2)
