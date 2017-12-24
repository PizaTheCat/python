from math import sqrt
inputNum = int(input("Type in the number: "))
xNum = inputNum
factors = []
for i in range(0, inputNum):
    for i in range(2, inputNum):
        temp = int(inputNum / i)
        if temp * i == inputNum:
            inputNum = temp
            factors.append(i)

for i0 in range(0, len(factors)):
    for i1 in range(2, factors[i0]):
        temp = int(factors[i0] / i1)
        if temp * i1 == factors[i0]:
            factors.remove(factors[i0])
            factors.append(i1)
            factors.append(temp)
factors.sort()
if len(factors) == 0:
    print("{0} is a prime number.".format(xNum))
else:
    print("{0} completely factorized is".format(xNum), end = ' ')
    for i in range(0, len(factors)):
        print(factors[i], end = ' ')
