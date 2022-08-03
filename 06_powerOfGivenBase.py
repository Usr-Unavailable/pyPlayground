# 6. Write a Python program to check if a number is a power of a given base.Go to the editor
# Input : 128,2
# Output : True
from math import log
def isPowerOfBase(n, b):
    boo = True if int(log(n, b)) == log(n, b) else False
    return boo
print(isPowerOfBase(128, 2))
print(isPowerOfBase(64, 2))
print(isPowerOfBase(12, 2))
