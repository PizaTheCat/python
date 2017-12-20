i = 0
pi = 3 * (10 ** 30)
n = 0
while True:
    i += 1
    n += 2
    temp = n * (n + 1) * (n + 2) #if n = 2 temp = 24
    temp = ((4 * (10 ** 30)) / temp) # 1/6 or 1.66667
    if i % 2 == 0:
        pi -= temp
    else:
        pi += temp
    if int(pi) != pi:
        break
    print(i)
    print(pi)
# i = 2
# print(i * (i+1) * (i+2))
# i += 1
# n += 2
# temp = n * (n + 1) * (n + 2) #if n = 2 temp = 24
# temp = 4 / temp # 1/6 or 1.66667
# if i % 2 == 0:
#     pi -= temp
# else:
#     pi += temp
# print(i)
# print(pi)
