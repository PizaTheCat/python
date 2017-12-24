input1 = int(input("Type in the first number: "))
input2 = int(input("Type in the second number: "))

factors1 = []
factors2 = []

for i in range(2, input1):
    temp = int(input1 / i)
    if temp * i == input1:
        factors1.append(i)

for i in range(2, input2):
    temp = int(input2 / i)
    if temp * i == input2:
        factors2.append(i)
answer = []
for i0 in range(0, len(factors1)):
    for i1 in range(0, len(factors2)):
        if factors1[i0] == factors2[i1]:
            answer.append(factors2[i1])
answer.reverse()
if len(answer) == 0:
    print("{0} and {1} have no common factors.".format(input1, input2))
else:
    answer = answer[0]
    print("The HCF of {0} and {1} is {2}.".format(input1, input2, answer))
