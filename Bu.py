from bs4 import BeautifulSoup as Soup
import requests

# from script.scraper import URL
Bu_facts = {}

URL = "https://www.bu.edu/president/boston-university-facts-stats/"

page = requests.get(URL)
soup = Soup(page.content, 'html.parser')
factsCategories = soup.find(class_ = "facts-categories")

categories = factsCategories.find_all('h5')

facts_list = factsCategories.find(class_ = "row list").text.strip()

for categori in categories :
    formatCategori = str(categori).replace("<h5>","").replace("</h5>","")
    Bu_facts[formatCategori] = None
    print(formatCategori)
print(facts_list.replace(",",""))    
print(Bu_facts)

