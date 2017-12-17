from datetime import datetime
from threading import Timer
from OWMfunction import weatherforcast
# day = x.day + 1, hour = 1, minute = 0, second + 10
x = datetime.today()
y = x.replace(x.minute + 30, second = 0)
delta_t = y - x
secs = delta_t.seconds + 1

t = Timer(secs, weatherforcast('Singapore'))
t.start()
