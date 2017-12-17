from random import randint
from allPrimesFrom1to10000000 import PrimesList
x = randint(1, len(PrimesList))
y = randint(1, len(PrimesList))
hugeNumber = PrimesList[x] * PrimesList[y]
