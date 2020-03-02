
"""
programa que valida un nombre de acuerdo a la cantidad de datos que hay en un conjunto.
"""
valid_alpha_user = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ1234567890-_."

while True:
    user = input("Ingrese el nombre de usuario: ")
    if (len(user)>4):
        a=set(valid_alpha_user)
        b=set(user)
        if len(b-a)>0:
            print("Usuario Invalido")
            continue
        else:
            print("Usuario Valido")
            break
    else:
        print("Usuario Invalido")