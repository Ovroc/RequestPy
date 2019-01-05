import requests
from bs4 import BeautifulSoup

url = "http://sp.olx.com.br/regiao-de-sao-jose-do-rio-preto"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

item = soup.find_all("a",{"class": "OLXad-list-link"})

for i in item:
    print (i.get("title"))
    print (i.get('href'))
    print("\n")
