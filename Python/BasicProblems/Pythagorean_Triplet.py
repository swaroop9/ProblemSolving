"""
Pythagorean Triplet in an array
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
Examples:
Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.


Trick:
odd : 7 squre 49 : 49/2 24.5 so 7,24, 25
even: 8 /2 =  4 4 square 16 +- 1 = 15 17 so 8 15 17"""

# Simple Solution
# def is_triplet(arr, n):
#     for i in range(n - 2):
#         print("I", i)
#         for j in range(i + 1, n - 1):
#             print("J", j)
#             for k in range(j + 1, n):
#                 print("K", k)
#                 x = arr[i] ** 2
#                 y = arr[j] ** 2
#                 z = arr[k] ** 2
#                 if x == y + z or y == x + z or z == y + x:
#                     print(arr[i], arr[j], arr[k])
#                     return True
#
#     return False
#
#
#
# arr = [25, 1, 7, 24, 7, 8]
# n = len(arr)
# print(is_triplet(arr, n))
# # is_triplet(arr, n) if print("Triplet") else print("Not a Triplet")

# Squre and sort
# import math
# from math import sqrt
#
#
# def is_triplet(arr, n):
#     # Step1
#     for i in range(n):
#         arr[i] = arr[i] ** 2
#
#     arr.sort()
#
#     for i in range(n - 1, 1, -1):
#         left = 0
#         right = n - 2
#         while left < right:
#             if arr[i] == arr[left] + arr[right]:
#                 print("Triplet: ", math.sqrt(arr[left]), ", ", math.sqrt(arr[right]), ", ", math.sqrt(arr[i]))
#                 left += 1
#                 right -= 1
#             elif arr[right] + arr[left] < arr[i]:
#                 left = left + 1
#             else:
#                 right -= 1
#
#
# arr = [25, 1, 7, 24, 7, 8]
# n = len(arr)
# is_triplet(arr, n)


# Method 3: (Using Hashing)

# Function to check if the
# Pythagorean triplet exists or not
import math


def checkTriplet(arr, n):
    maximum = 0

    # Find the maximum element
    for i in range(n):
        maximum = max(maximum, arr[i])

        # Hashing array
    hash = [0] * (maximum + 1)

    # Increase the count of array elements
    # in hash table
    for i in range(n):
        hash[arr[i]] += 1

        # Iterate for all possible a
    for i in range(1, maximum + 1):
        # If a is not there
        if hash[i] == 0:
            continue

        # Iterate for all possible b
        for j in range(1, maximum + 1):
            # If a and b are same and there is only one a
            # or if there is no b in original array
            if (i == j and hash[i] == 1) or hash[j] == 0:
                continue

            # Find c
            val = int(math.sqrt(i * i + j * j))

            # If c^2 is not a perfect square
            if (val * val) != (i * i + j * j):
                continue

            # If c exceeds the maximum value
            if val > maximum:
                continue

            # If there exists c in the original array,
            # we have the triplet
            if hash[val]:
                return True
    return False


# Driver Code
arr = [3, 2, 4, 6, 5]
n = len(arr)
if checkTriplet(arr, n):
    print("Yes")
else:
    print("No")


# # triplet in ar[0..n-1]
#
# def isTriplet(ar, n):
#     j = 0
#
#     for i in range(n - 2):
#         for k in range(j + 1, n):
#             for j in range(i + 1, n - 1):
#                 # Calculate square of array elements
#                 x = ar[i] * ar[i]
#                 y = ar[j] * ar[j]
#                 z = ar[k] * ar[k]
#                 if (x == y + z or y == x + z or z == x + y):
#                     return 1
#
#     # If we reach here, no triplet found
#     return 0
#
#
# # Driver program to test above function
# ar = [3, 1, 4, 6, 5]
# ar_size = len(ar)
#
# if (isTriplet(ar, ar_size)):
#     print("Yes")
# else:
#     print("No")
