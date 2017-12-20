i = 0
pi = 3
n = 0
while True:
    i += 1
    n += 2
    temp = i * (i + 1) * (i + 2)
    temp = 4 / temp
    if i % 2 == 0:
        pi -= temp
    else:
        pi += temp
    print(i)
    print(pi)
