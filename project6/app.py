

string cripto1, cripto2, cripto3

int cant1, cant2, cant3

cripto1 = read(“ingrese el nombre la primera moneda: “)
cripto2 = read(“ingrese el nombre la segunda moneda: “)
cripto3 = read(“ingrese el nombre la tercer moneda: “)
cant1 = int(read(“Ingrese la cantidad de la primera moneda: “))
cant2 = int(read(“Ingrese la cantidad de la segunda moneda: “))
cant3 = int(read(“Ingrese la cantidad de la tercer moneda: “))
if cant1 > cant2 y cant1 > cant3 then
print(cripto1+”: “+cant1)
if cant2 > cant3 then
print(cripto2+”: “+cant2)
print(cripto3+”: “+cant3)
else
print(cripto3+”: “+cant3)
print(cripto2+”: “+cant2)
endif
elseif cant2 > cant1 y cant2 > cant3
print(cripto2+”: “+cant2)
if cant1 > cant3 then
print(cripto1+”: “+cant1)
print(cripto3+”: “+cant3)
else
print(cripto3+”: “+cant3)
print(cripto1+”: “+cant1)
endif
else
print(cripto3+”: “+cant3)
if cant1 > cant2 then
print(cripto1+”: “+cant1)
print(cripto2+”: “+cant2)
else
print(cripto2+”: “+cant2)
print(cripto1+”: “+cant1)
endif
endif