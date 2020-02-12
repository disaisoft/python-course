
"""Escribe un programa en Python que dada una criptomoneda, la cantidad acumulada 
y su correspondiente cotización por dólar del día, le permita al usuario conocer la
fecha completa y hora del momento en que obtuvo el sistema esa información."""

from datetime import datetime
nombreCripto=input("Nombre de la Criptomoneda: ")
cantCripto=float(input("Cantidad acumulada de la Criptomoneda: "))
cotizacion=float(input("Cotización por US$ del día de la Criptomoneda: "))
ahora = datetime.now()

print("La fecha completa y la hora en la que obtuvo la informacion fue: " 
+ahora.strftime("%A, %d de %B de %Y a las %I:%M:%S%p"))






