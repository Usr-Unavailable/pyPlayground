# 5. Write a Python program to check if an integer is the power of another integer.Go to the editor
# Input : 16, 2
# Output : True

import math

def isPowerOfAnotherInteger(n, k):
    boo = True if int(math.log(n, k)) == math.log(n, k) else False
    return boo
print(isPowerOfAnotherInteger(16, 2))
print(isPowerOfAnotherInteger(14, 2))
print(isPowerOfAnotherInteger(9, 3))

