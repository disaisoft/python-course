

x=int(input("Indique el primer numero: "))
y=int(input("Indique el segundo numero: "))
z=int(input("Indique el tercer numero"))

print("El maximo entre", x,",",y,"y",z,"es",max(max(x,y),z))

def max(a,b):
    """Esta funcion calcula el maximo entre dos numeros"""
    if a>b:
        maximo=a 
    else:
        maximo=b
    return maximo