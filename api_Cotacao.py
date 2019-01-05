import requests
import json

req = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

#print(req.text)
cotacao = json.loads(req.text)

dolar = cotacao['valores'] ['USD']["valor"]
euro = cotacao['valores'] ['EUR']["valor"]
peso = cotacao['valores'] ['ARS']["valor"]
libra = cotacao['valores'] ['GBP']["valor"]
bit= cotacao['valores'] ['BTC']["valor"]

print('##### COTACAO #####')
print ("Dolar : "+str(dolar))
print ("Euro : "+str(euro))
print ("Peso : "+str(peso))
print ("Libra : "+str(libra))
print ("BitCoin : "+str(bit))