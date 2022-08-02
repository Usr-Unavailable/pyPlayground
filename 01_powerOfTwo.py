import math

# https://www.w3resource.com/python-exercises/challenges/1/index.php
# 1. Write a Python program to check if a given positive integer is a power of two. 
# Input : 4
# Output : True

def isPowerOfTwo(n):
    boo = False
    if int(math.log(n, 2)) == math.log(n, 2):
        boo = True
    return boo
print(isPowerOfTwo(4))
print(isPowerOfTwo(6))
print(isPowerOfTwo(8))
