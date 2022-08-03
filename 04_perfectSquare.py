# 4. Write a Python program to check if a number is a perfect square. Go to the editor
# Input : 9
# Output : True

def isPerfectSquare(n):
    boo = False
    if int(n ** 0.5) == n ** 0.5:
        boo = True
    return boo
print(isPerfectSquare(4))
print(isPerfectSquare(6))
print(isPerfectSquare(9))