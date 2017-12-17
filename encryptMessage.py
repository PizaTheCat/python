# import string
import letterToNumDict as LTND
from randomPicker import *
# dict1 = dict(enumerate(string.ascii_lowercase, 1))
# print(dict1[3])

print(LTND.letterToNum['a'])
message = input("Please input your message: ")
list1 = list(message)
list2 = []
for i in range(0, len(list1)):
    list2.append(LTND.letterToNum[list1[i]])
list1 = []
for i in range(0, len(list2)):
    list1.append(list2[i] ** 257)
list2 = []
for i in range(0, len(list1)):
    list2.append(list1[i] % hugeNumber)
E = 257
# D = ((x-1) * (y-1))
# D = D + 1
# D = D / E
i = 0
while True:
    i += 1
    D = ((x-1) * (y-1)) * i
    D += 1
    if D % E == 0:
        break
D = D / E
print(D)
print(hugeNumber)
print((list2[1]**D) % hugeNumber)
