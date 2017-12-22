import datetime
temp = str(datetime.datetime.now())
c1 = list(temp)
temp = int((int(c1[20]) + 5) / (int(c1[21]) + 4) * (int(c1[22]) + 3) / (int(c1[23]) + 2) * (int(c1[24]) + 1) / (int(c1[25]) + 1))
print(temp)
n = int(c1[20])
for i in range(1, 6):
    n = n ** int(c1[20 + i])
if temp != 0:
    temp = n * temp
temp /= int(c1[20])
print(temp)
