n = 1
trueFalse = 1
while trueFalse == 1:
    n += 1
    print(n)
    if n % 10**9 == 0:
        trueFalse = 0
        inputX = input("Continue? Yes or No: ")
        if str(inputX) == 'Yes':
            trueFalse = 1
