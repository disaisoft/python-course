"""Escribe un programa en Python que dada una criptomoneda, 
la cantidad acumulada y su correspondiente cotización por dólar
del día, le permita al usuario conocer la fecha completa y hora
del momento en que obtuvo el sistema esa información, así como el
monto en US$ que tiene el usuario en su billetera digital. Considerando
un crecimiento del 5% por día, muéstrale al usuario para ese mismo día de
la siguiente semana cuál sería su ganancia en US$.

Recomendaciones:

Considera el módulo datetime de Python
Recuerda las operaciones de lectura y escritura
Escribe los resultados en un formato adecuado para el usuario """

from datetime import datetime

nombreCripto=input("Nombre de la Criptomoneda: ")
cantCripto=float(input("Cantidad acumulada de la Criptomoneda: "))
cotizacion=float(input("Cotización por US$ del día de la Criptomoneda: "))
ahora = datetime.now()
print("La fecha completa y hora en la que obtuvo la informacion fue: " +str(ahora))
valorTotal= cantCripto * cotizacion
print("Ud. Posee un total de US$ "+str(valorTotal))
valorTotal1=valorTotal*1.05
valorTotal2=valorTotal1*1.05
valorTotal3=valorTotal2*1.05
valorTotal4=valorTotal3*1.05
valorTotal5=valorTotal4*1.05
valorTotal6=valorTotal5*1.05
valorTotal7=valorTotal6*1.05
ganancia= valorTotal7-valorTotal
print("Su ganancia luego de una semana es: "+str(ganancia)+" USD")

