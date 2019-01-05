import requests
from bs4 import BeautifulSoup


url = "http://www.cptec.inpe.br/cidades/tempo/4956"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

t= soup.find_all("div",{"class":"c2"})
u= soup.find_all("div",{"class":"c3"})
s= soup.find_all("div",{"class":"c4"})
d= soup.find_all("div",{"class":"c7"})

top = (soup.title.get_text() +'  | '  + d[0].text)
down = (t[0].text +'  | '  + u[0].text +'  | '  + s[0].text)

print (""+top+"\n"+down)
