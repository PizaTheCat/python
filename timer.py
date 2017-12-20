from datetime import datetime
# from threading import Timer
from OWMfunction import weatherforcast
import time as t
# day = x.day + 1, hour = 1, minute = 0, second + 10
# x = datetime.today()
# y = x.replace(second = x.second + 5)
# delta_t = y - x
# secs = delta_t.seconds + 1
#
# t = Timer(secs, weatherforcast('Singapore'))
# # t.start()
# from threading import Timer
# weatherforcast('Singapore')
# t = Timer(60.0, weatherforcast('Singapore'))
# t.start
while True:
    weatherforcast('Singapore')
    t.sleep(600)
