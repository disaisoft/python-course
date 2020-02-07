
""" Te proponemos escribir un programa en Python que nos permita calcular 
la ganancia de una criptomoneda (Nombre y Cantidad), si ésta se negocia por 
una cantidad de días indicada por el usuario y a una ganancia fija indicada 
también por el usuario. Al terminar, el programa debe indicar la ganancia en 
cantidad de criptomoneda, la cantidad de días negociados y el monto total al 
finalizar los días.

Recomendaciones:
Asigna a las variables nombres nemotécnicos; es decir; que describan su contenido
En Python no hay declaración de variables, se crean asignando el valor deseado
Hacer las lecturas y escrituras correspondientes. """


cripto = input("Indique el nombre de la moneda: ")
cant = float(input("Indique la cantidad de la moneda que posee: "))
dias = int(input("Indique la cantidad de días que negociará la moneda: "))
ganancia = float(input("Indique el porcentaje de ganancia esperada por día: "))


ganancia_total = cant*ganancia/100*dias
cant_total = cant + ganancia_total

print("La ganancia de",cripto,"durante los ",str(dias),"es",str(ganancia_total))
print("El monto total de",cripto,"a los",str(dias),"es de",str(cant_total))