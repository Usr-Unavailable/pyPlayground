import math

# https://www.w3resource.com/python-exercises/challenges/1/index.php
# 1. Write a Python program to check if a given positive integer is a power of two. 
# Input : 4
# Output : True

def isPowerOfThree(n):
    boo = False
    if int(math.log(n, 3)) == math.log(n, 3):
        boo = True
    return boo
print(isPowerOfThree(3))
print(isPowerOfThree(6))
print(isPowerOfThree(9))
