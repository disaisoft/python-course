"""
Escribe un programa en Python que dada una criptomoneda y 
un monto en esa criptomoneda, permita incrementar el saldo de tu teléfono móvil. 
Considera que los pagos pueden ser realizados mediante bitcoin (BTC), dash (DASH)
o litecoin (LTC). 
"""


BTCUSD=7630.80
DASHUSD=315.56
LTCUSD=120.84
moneda=input("Ingrese la moneda a utilizar(BTC, DASH o LTC): ");
if moneda=="BTC" or moneda=="DASH" or moneda=="LTC":
    cantidad=float(input("Ingrese la cantidad a utilizar: "));
    if moneda=="BTC":
        monto=cantidad * BTCUSD;
    elif moneda=="DASH":
        monto=cantidad * DASHUSD;
    else:
        monto=cantidad * LTCUSD;
    print("La cantidad de USD recargado fue de: "+str(monto));
else:
    print("Error: Solo se permite utilizar BTC, DASH o LTC");
