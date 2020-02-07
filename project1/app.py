
""" Escribe un programa en Python que le permita al usuario conocer el monto en dólares americanos que tiene acumulado 
en su wallet o billetera digital correspondiente a una criptomoneda particular. En tal sentido, el programa debe leer 
el nombre de la criptomoneda, la cantidad acumulada de esa criptomoneda y su cotización por US$ del momento. Luego,
debe calcular el monto total en US$ que posee el usuario e imprimir el siguiente mensaje: “Ud. posee un total de US$”
seguido del cálculo realizado.

Recomendaciones:

Asigna a las variables nombres nemotécnicos; 


es decir; que describan su contenido
En Python no hay declaración de variables, se """

nombreCripto = input("Nombre de la Criptomoneda: ")
cantCripto = float(input("Cantidad acumulada de la Criptomoneda: "))
cotizacion = float(input("Cotización por US$ del día de la Criptomoneda: "))
valorTotal= cantCripto * cotizacion
print("Ud. Posee un total de US$ "+str(valorTotal))

