import math

# https://www.w3resource.com/python-exercises/challenges/1/index.php
# 3. Write a Python program to check if a given positive integer is a power of four. Go to the editor
# Input : 4
# Output : True

def isPowerOFour(n):
    boo = False
    if int(math.log(n, 4)) == math.log(n, 4):
        boo = True
    return boo
print(isPowerOFour(4))
print(isPowerOFour(6))
print(isPowerOFour(8))
