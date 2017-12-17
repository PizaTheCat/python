maxNumToCheck = 1000
from math import pow as p
for i in range(1, maxNumToCheck + 1):
    num = list(str(i))
    numberOfDigitsInMaxNumToCheck = len(num)
    total = 0
    for j in range (0, numberOfDigitsInMaxNumToCheck):
        total = total + pow(int(num[j]), numberOfDigitsInMaxNumToCheck)
    if total == i:
        endList.append(i)
        print(endList)
        print(i)
print(endList)
