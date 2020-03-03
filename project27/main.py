
"""
Tipo de dato estructurado - Diccionarios
"""

import requests

def esmoneda(cripto):
    return cripto in monedas 

monedas=()
monedas_dic={}

data=requests.get("https://api.coinmarketcap.com/v2/ticker/").json()
for id in data["data"]:
    monedas_dic[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["price"]

monedas=monedas_dic.keys()

moneda=input("Indique el nombre de la moneda a obtener: ")
while not esmoneda(moneda):
    print("Moneda Invalida")
    moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol: ",moneda,
    "tiene un precio de: ",monedas_dic.get(moneda),"USD")