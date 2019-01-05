import requests
import json

usr = input("Informe o CEP: ")
Cep = str(usr)
r = requests.get('http://correiosapi.apphb.com/cep/'+Cep)
d = json.loads(r.text)

print ("\n")
print("CEP: "+d['cep'])
print(d['tipoDeLogradouro'] + " "+ d['logradouro'])
print("Bairro: "+ d['bairro'])
print("Cidade: "+d['cidade']+" -" + d['estado'])
print ("\n")

