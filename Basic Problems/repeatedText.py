# Python program to return the maximum occurring character in the input string
ASCII_SIZE = 256


def getMaxOccuringChar(str):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * ASCII_SIZE

    # Utility variables
    max_val = -1
    c = ''

    # Traversing through the string and maintaining the count of
    # each character
    for i in str:
        count[ord(i)] += 1;

    for i in str:
        if max_val < count[ord(i)]:
            max_val = count[ord(i)]
            c = i

    return c


# Driver program to test the above function
str = "sample string"
print("Max occurring character is " + getMaxOccuringChar(str))

# Although this program can be written in atmost 3 lines in Python
# the above program has been written for a better understanding of
# the reader

# Shorter version of the program
# import collections
# str = "sample string"
# print "Max occurring character is " +
#	 collections.Counter(str).most_common(1)[0][0]


# def maxPoints(elements):
#     # Write your code here
#
#     print(elements)
#     max_point = 0
#
#     while elements:
#         max_value = max(elements)
#         for value in elements:
#             if value == max_value:
#                 max_point += max_value
#                 elements.remove(value)
#                 for val in elements:
#                     if val == (max_value + 1) or val == (max_value - 1):
#                         elements.remove(val)
#
#     return max_point
#
#
# print(maxPoints([3, 4, 2]))
