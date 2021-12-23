"""Python3 program to find the repeating and missing elements"""

# Method #1
"""Approach:Find the repeating and missing elements using Maps"""


def findRepeatingAndMissingElement(arr):
    numberMap = {}
    maxElement = len(arr)

    for ele in arr:
        if numberMap.get(ele):
            print("Repeating = ", ele)
        else:
            numberMap[ele] = True

    for i in range(1, maxElement + 1):
        if not i in numberMap:
            print("Missing = ", i)

arr = [4, 3, 6, 2, 1, 1,2]
findRepeatingAndMissingElement(arr)

# Method 2 (Use Sorting)
"""Approach: Sort the input array. Traverse the array and check for missing and repeating."""


def findRepeatingAndMissingElement_2(arr):
    sortedArr = sorted(arr)

    for i in range(1, len(arr)):
        if sortedArr[i - 1] == sortedArr[i]:
            print("Repeated", i)
        elif not i in sortedArr:
            print('Missing', i)
arr = [4, 3, 6, 2, 1, 1, 2]
findRepeatingAndMissingElement_2(arr)
