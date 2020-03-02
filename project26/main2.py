
"""
Escribe un programa en Python que solicite al usuario el nombre de una criptomoneda y 
verifique si ésta existe en coinmarketcap.com. Posteriormente, el programa debe imprimir 
el nombre abreviado o, como también se conoce, nombre código y el nombre completo de la criptomoneda. 
Para esto, recuerda utilizar el módulo requests, usando la API https://api.coinmarketcap.com/v2/listings/ 
que retorna un json con una lista de datos de las criptomonedas. Entre estos datos tenemos el symbol de la
 criptomoneda que corresponde al nombre código y name que contiene el nombre completo de la criptomoneda.
"""

import requests

def esmoneda(cripto):
    return cripto in monedas

monedas=()
monedas_dict={}

data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
for cripto in data["data"]:
    monedas_dict[cripto["symbol"]]=cripto["name"]

monedas = monedas_dict.keys()

moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:,",moneda,"y nombre:",monedas_dict.get(moneda),
          "es valida porque existe en coimnmarketcap.com")
