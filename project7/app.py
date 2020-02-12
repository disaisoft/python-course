

"""En tal sentido, te solicitamos que escribas un programa en pseudocódigo
que reciba cinco criptomonedas, cada una con sus respectivas cantidades y precios
en dólares americanos (USD), y luego imprima el valor total en USD que tienes acumulado.

Recomendaciones:

Considera el uso de ciclos iterativos
Recuerda las operaciones de lectura y escritura """



cripto = ""
cant, cotiz, valor = "","",""
i = 0
i=0
valor=0.0
while i < 5 : 
    cripto = input("ingrese el nombre la moneda: ")
    cant = float(input("Ingrese la cantidad de la moneda: "))
    cotiz = float(input("Ingrese la cotización en USD de la moneda: "))
    valor = valor + (cant*cotiz)

print("Usted tiene “+valor+” Dólares Americanos")