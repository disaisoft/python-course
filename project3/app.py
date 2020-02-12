from datetime import date
from datetime import datetime

#obtener la fecha actual.
d = date.today()
d.strftime("/%d/%m/%y")
print(d)

# obtener la fecha con el dia, mes, ano y la hora
dt=datetime.now()
dt.strftime("%A %d/%B/%y %H:%M:%S")
print(dt)