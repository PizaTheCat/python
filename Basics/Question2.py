# https://en.wikipedia.org/wiki/Fermat_number
# Check Fermat number if they are prime number
# F0	=	2^1	+	1	=	3 is prime
# F1	=	2^2	+	1	=	5 is prime
# F2	=	2^4	+	1	=	17 is prime
# F3	=	2^8	+	1	=	257 is prime
# F4	=	2^16	+	1	=	65,537 is the largest known Fermat prime
# F5	=	2^32	+	1	=	4,294,967,297
# F6	=	2^64	+	1	=	18,446,744,073,709,551,617 (20 digits)
#                           =	274,177 × 67,280,421,310,721 (14 digits) (fully factored 1855)

maxNumCheck = 1000000
primeArray = [2]
# assume the number is a prime number
isPrime = 1

countToPrintToConsole = 0;

print("Building prime array...")
for i in range(3, maxNumCheck):
    countToPrintToConsole = countToPrintToConsole + 1
    if (countToPrintToConsole >= 100000):
        print("Checking " + str(round(i, -1)));
        countToPrintToConsole = 0;
    isPrime = 1
    for j in range(0, len(primeArray)-1):
        if ((primeArray[j] * primeArray[j]) > i):
            break;
        x = i / primeArray[j]
        if x == int(x):
            isPrime = 0
            break
    if isPrime == 1:
        primeArray.append(i)
print(primeArray)
print(len(primeArray))
f = open("allPrimesFrom1to10000000.txt")
with open("allPrimesFrom1to10000000.txt",'w',encoding = 'utf-8') as f:
    for i in primeArray:
        f.write(primeArray(i))
