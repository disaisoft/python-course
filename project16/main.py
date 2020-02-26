""" 
Escribe un programa en Python que solicite el ingreso de tres criptomonedas, 
las cantidades y cotizaciones en Dólares Americanos (USD) de cada una de éstas, 
validando que las tres criptomonedas pertenezcan a las siguientes 
(BTC, BCC, LTC, ETH, ETC y XRP), y que las cantidades y cotizaciones 
sean números reales. Por último el programa debe indicar la cantidad 
de USD que el usuario tiene acumulado.
"""

criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
i=0
total=0
while (i < 3):
    cripto = input("Ingrese el nombre de la moneda: ")
    if cripto in criptos:
        i=i+1
        cant=""
        while not cant.replace('.','',1).isdigit():
            cant = input("Indique la cantidad de  "+cripto+":")
        else:
            cotiz=""
            while not cotiz.replace('.','',1).isdigit():
                cotiz = input("Indique la cotización en USD de "+cripto+":")
            else:
                total = total + float(cant) * float(cotiz)
    else:
        print("Moneda invalida.")
print("El tota en USD que tiene el usuario es de ",str(total))