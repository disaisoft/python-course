"""
En esta oportunidad te pedimos escribir un programa en pseudocódigo que 
registre el nombre de cinco criptomonedas, con sus respectivas cantidades 
y precios en USD, haciendo uso de arreglos. Posteriormente, imprima los datos 
de cada moneda luego de ser ingresadas por el usuario.
"""

cripto [5]
cant[5], cotiz[5]
i=0

while i<5 do
    cripto[i]=read("Ingrese el nombre de la moneda: ")
    cant[i]=float(read("Ingrese la cantidad de "+cripto[i]+":")
    cotiz[i]=float(read("Ingrese la cotización en USD de "+cripto[i]+":")
    i=i+1
endwhile
i=0
while i<5 do
    print("Moneda: "+cripto[i]+", cantidad: "+cant[i]+", precio en USD: "+cotiz[i])
    i=i+1
endwhile