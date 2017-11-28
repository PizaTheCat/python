import math
maxNumCheck = 1000
c = [2,3]
b = []
check = 1
y = 0
z = 0
x = -1
for i in (2, maxNumCheck):
    for j in (2, len(c)):
        x = x + 1
        y = i / c[-x]
        z = round(y, 0)
        if z == y:
            check = 0
            b.append(i)
            break
    if check == 1:
        c.append(i)
    check = 1
print(i)
print(j)
print(c)
print(b)
print(z)
print(y)
