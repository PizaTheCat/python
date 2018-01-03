from collections import Counter
from math import sqrt
input1 = int(input("Type in the first number: "))
input2 = int(input("Type in the second number: "))

factors1 = []
for i in range(0, input1):
    for i in range(2, input1):
        temp = int(input1 / i)
        if temp * i == input1:
            input1 = temp
            factors1.append(i)
for i0 in range(0, len(factors1)):
    for i1 in range(2, factors1[i0]):
        temp = int(factors1[i0] / i1)
        if temp * i1 == factors1[i0]:
            factors1.remove(factors1[i0])
            factors1.append(i1)
            factors1.append(temp)
            factors1.sort()
            print(factors1)
factors2 = []
for i in range(0, input2):
    for i in range(2, input2):
        temp = int(input2 / i)
        if temp * i == input2:
            input2 = temp
            factors2.append(i)
for i0 in range(0, len(factors2)):
    for i1 in range(2, factors2[i0]):
        temp = int(factors2[i0] / i1)
        if temp * i1 == factors2[i0]:
            factors2.remove(factors2[i0])
            factors2.append(i1)
            factors2.append(temp)
            factors2.sort()
            print(factors2)
def exponents ( factors ):
    answer = []
    x = 0
    trueORfalse = 0
    for i in range(0, len(factors) - 1):
        if trueORfalse == 0:
            n = factors[i]
            trueORfalse = 1
            x += 1
            continue
        else:
            if n == factors[i]:
                x += 1
            else:
                trueORfalse = 0
                answer.append(n)
                answer.append(x)
                x = 0
    return(answer)
answer1 = []
answer2 = []
answer1 = exponents(factors1)
answer2 = exponents(factors2)
commonNums = list(set(answer1).intersection(answer2))
uncommonNums = list((Counter(answer1) - Counter(answer2)).elements())
print(commonNums)
print(uncommonNums)
# def checkIfWholeNum( num ):
#     if num == int(num):
#         return num
#     else:
#         n = num
#         while True:
#             n *= 2
#             if n == int(n):
#                 break
#         return n
# if input1 > input2:
#     n = input1 - input2
#     i = 1
#     n = input1 / n
# else:
#     n = input2 - input1
#     i = 0
#     n = input2 / n
# n = checkIfWholeNum(n)
# if i == 1:
#     answer = input2 * n
# else:
#     answer = input1 * n
# # print(n)
# print("The LCM of {0} and {1} is {2}.".format(input1, input2, int(answer)))
