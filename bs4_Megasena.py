# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

"""
for b in box:
    concurso = box.find_all({"h2":"class"})
game = []
for c in concurso:
    game = c.text

print game.strip()
"""
def Awards():
    box = soup.find("div", {"class":"related-box gray-text no-margin"})
    item = box.find("p",{"class":"description"})
    lista = []
    for i in item:
        lista = i

    print lista.strip()


def Head():
    head_A = soup.title.text
    print (head_A)

def Num_mega():
    numbers = soup.find_all("ul",{"class":"numbers mega-sena"})
    l = []
    for num in numbers :
        l  = num.get_text()
        print (l[0]+l[1]+"-"+l[2]+l[3]+"-"+l[4]+l[5]+"-"+l[6]+l[7]+"-"+l[8]+l[9]+"-"+l[10]+l[11]) #Lista dos numeros Sorteados

def Valor_prox():    #Valor da Premiação do Proximo Concurso
    next_concurso = soup.find_all("div",{"class":"next-prize clearfix"})
    for n in next_concurso:
        search = n.find_all("p",{"class":"value"})

    for ss in search:
        print ss.get_text()



Head()

print("\n")
print ("Dezenas Sorteadas")
Num_mega()
print ("\nSena - 6 números acertados")
Awards()
print ("\nEstimativa de prêmio do próximo concurso ")
Valor_prox()
print("\n\n")
