import requests
from bs4 import BeautifulSoup

url = "http://globoesporte.globo.com/plantao.html"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

links = soup.find_all("a", {"class": "feed-post-link"})

for link in links:
    print("\n")
    print(link.get_text())
    print (link.get('href'))


