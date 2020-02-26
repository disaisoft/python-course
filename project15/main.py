""" 
Escribe un programa en Python que dados el nombre de una criptomoneda 
y su monto inicial para un usuario, genere un porcentaje aleatorio entre
0 y 3%, además puede ser de alza o baja, asociado a esa criptomoneda e 
imprima el porcentaje diario durante una semana, si es alza o baja, el 
saldo diario de la billetera digital del usuario y el total acumulado en esa semana.
"""

import random
print("Text")
moneda=input("Ingrese la moneda: ")
cantidad=float(input("Ingrese la cantidad de "+moneda+": "))
count=0
while count < 7:
    profit=random.uniform(-0.03,0.03)
    cantidad=cantidad+(cantidad*profit)
    count=count+1
    print("Saldo de",moneda,"el dia",count,"es de: %6.7f"%cantidad+". Ganacia de %6.2f"%(profit*100),"%")
