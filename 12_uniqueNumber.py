# 12. Write a Python program to find the single number in a list that doesn't occur twice.Go to the editor
# Input : [5, 3, 4, 3, 4]
# Output : 5

def getUniqueNumber(lst):
    result = 0
    for _ in lst:
        result ^= _
    return result
lst = [5, 3, 4, 3, 4]
print(getUniqueNumber(lst))