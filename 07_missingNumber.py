# 7. Write a Python program to find a missing number from a list. Go to the editor
# Input : [1,2,3,4,6,7,8]
# Output : 5

def findMissingNumberFromList(lst):
    fullList = [*range(lst[0], lst[-1] + 1)]
    diff = set(fullList) - set(lst)
    return min(diff)
lst = [1,2,3,4,6,7,8]
print(findMissingNumberFromList(lst))