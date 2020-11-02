""" How to shift elements in a list in Python """

# Method #1

arrayIn = [1, 2, 3, 4, 5, 6]  # arrayOut = [4, 5, 6, 1, 2, 3]
shift = 3

arrayLength = len(arrayIn)

for i in range(0, shift):
    last = arrayIn[arrayLength - 1]
    for x in range(arrayLength - 1, -1, -1):
        # print(x)
        arrayIn[x] = arrayIn[x - 1]
    arrayIn[0] = last

print(arrayIn)

# Method #2

"""
USE collections.deque TO SHIFT ELEMENTS --> https://www.kite.com/python/docs/collections.deque
Call collections.deque() on a list to return a deque object.

Call collections.deque.rotate(n) to shift elements n times to the right if n is positive and left if n is negative.

Then call list() on the collections.deque to convert it to a list.
"""
import collections

a_list = collections.deque([1, 2, 3, 4, 5])

a_list.rotate(2)  # Shift `a_list` 2 places to the right

shifted_list = list(a_list)

print(shifted_list)

a_list = collections.deque([1, 2, 3, 4, 5])

a_list.rotate(-2)  # Shift `a_list` 2 places to the left

shifted_list = list(a_list)

print(shifted_list)
