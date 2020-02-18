

""" Te presentamos la definición de una función escrita en pseudo-código 
denominada ConversionCriptomoneda (…) que permite convertir una cantidad
de dinero dada en bitcoins y ripples a dólares americanos; retornando el 
monto total resultante de la suma de los dosvalores calculados en dólares
 americanos. Estas son las equivalencias aproximadas:

1 bitcoin = 7,442.50 USD$
1 ripple=0.660982 USD$
Puedes hacer uso del siguiente código base:

funcion ConversionCriptomoneda(cantBTC,cantXRP: float):
   Var saldoTotalUSD,BTCUSD,XRPUSD: float;
   BTCUSD=7442.50
   XRPUSD=0.660982;

   saldoTotalUSD;
finFuncion """



funcion (ConversionCrip) (cantBTC,cantXRP: float): float
var saldoTotalUSD, BTCUSD,XRPUSD: float;
BTCUSD=7442.50;
XRPUSD=0.660982;
saldoTotalUSD = (cantBTC*BTCUSD) + (cantXRP*XRPUSD);
retorna saldoTotalUSD;
finFuncion