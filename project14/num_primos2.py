inf = int(input("Limite inferior del intervalo: "))
sup = int(input("Limite superior del intervalo: "))
print("Los numeros primos entre",inf,"y",sup,"son: ")
for num in range(inf,sup+1):
    for i in range(2,num):
        if (num%i)==0:
            break
        elif i == num-1:
            print(num,"es un numero primo")