from email import header
from turtle import title
from wsgiref import headers
from bs4 import BeautifulSoup
import smtplib
import requests


URL = "https://www.amazon.in/Logitech-Silent-Wireless-Mouse-Charcoal/dp/B01M72LILF/ref=sr_1_3?keywords=logitech%2Bmouse&qid=1654105234&s=electronics&sprefix=logi%2Celectronics%2C204&sr=1-3&th=1"
headers = {"User-Agenet": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
title = soup.find(id = "productTitle").getText()
# a-price-whole
price = soup.find( class_ = "a-offscreen" ).get_text()
cost = float(price[1:6].replace(',',''))


# if(cost<3700):
#     send_mail()


print("Product:- ")
print(title.strip())
print("price:- ",cost)




# def send_mail():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login('ed.magician@gmail.com')
