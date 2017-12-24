input1 = int(input("Type in the first number: "))
input2 = int(input("Type in the second number: "))

def checkIfWholeNum( num ):
    if num == int(num):
        return num
    else:
        n = num
        while True:
            n *= 2
            if n == int(n):
                break
        return n
if input1 > input2:
    n = input1 - input2
    i = 1
    n = input1 / n
else:
    n = input2 - input1
    i = 0
    n = input2 / n
n = checkIfWholeNum(n)
if i == 1:
    answer = input2 * n
else:
    answer = input1 * n
print("The LCM of {0} and {1} is {2}.".format(input1, input2, int(answer)))
