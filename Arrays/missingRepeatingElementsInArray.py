"""Python3 program to find the repeating and missing elements"""

# Method #1
"""Approach:Find the repeating and missing elements using Maps"""


def main():
    arr = [4, 3, 6, 2, 1, 1,2]

    numberMap = {}
    maxElement = len(arr)

    for i in arr:

        if not i in numberMap:
            numberMap[i] = True

        else:
            print("Repeating = ", i)

    for i in range(1, maxElement + 1):
        if not i in numberMap:
            print("Missing = ", i)


main()

# Method 2 (Use Sorting)
"""Approach: Sort the input array. Traverse the array and check for missing and repeating."""


def main():
    arr = [4, 3, 6, 2, 1, 1]

    sortedArr = sorted(arr)

    for i in range(1, len(arr)):

        if not i in sortedArr:
            print('Missing', i)

        if sortedArr[i - 1] == sortedArr[i]:
            print("Repeated", i)


main()
