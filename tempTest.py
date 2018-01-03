import sys
def sizeof(x):
    print(x.__class__, sys.getsizeof(x), x)
sizeof(list)
