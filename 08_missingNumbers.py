# 8. Write a Python program to find missing numbers from a list. Go to the editor
# Input : [1,2,3,4,6,7,10]
# Output : [5, 8, 9]

def findMissingNumberFromList(lst):
    fullList = [*range(lst[0], lst[-1] + 1)]
    diff = list(set(fullList) - set(lst))
    diff.sort()
    return diff
lst = [1,2,3,4,6,7,10]
print(findMissingNumberFromList(lst))