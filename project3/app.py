from datetime import date
from datetime import datetime

#obtener la fecha actual.
d = date.today()
d.strftime("/%d/%m/%y")
print(d)

# obtener la fecha con el dia y la hora
dt=datetime.now()
dt.strftime("%A %d/%m/%y %H:%M:%S")