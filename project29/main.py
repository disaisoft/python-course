
"""h
ejercicio #29, Este ejercicio consiste en escribir un programa en Python que construya 
un glosario de términos pertenecientes al mundo de las criptomonedas con sus correspondientes 
significados y, a la vez, permita consultar un término dado por el usuario. 
En el caso que no existe el término solicitado, se le da la posibilidad al 
usuario de incorporar este término con su correspondiente significado.
"""

nombre_archivo = "Glosario.txt"
archivo = open(nombre_archivo,"r")

texto = archivo.read()
archivo.close()
lineas = texto.splitlines()
terminos = texto.split(":")
diccionario={}
for linea in lineas:
    termino = linea.split(":")
    diccionario[termino[0]]=termino[1]

buscar = input("Indique el termino a buscar en el diccionario: ")
encontrado = diccionario.get(buscar)
if encontrado:
    print(buscar+":"+" "+encontrado)
else:
    print("Termino no existe ene l glosario")
    ingresar_termino = input("Desea ingresar este termino(s/n):")
    if (ingresar_termino=='s'):
        archivo = open(nombre_archivo,"a")
        nuevo_termino = input("Indique la descripción del termino "+buscar+":")
        archivo.write("\n"+buscar+":"+nuevo_termino)
        archivo.close()