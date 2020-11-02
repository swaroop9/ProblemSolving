# Python3 program to find the
# # repeating and missing elements
# # using Maps
# # numberMap = {}
# def main():
#     arr = [4, 3, 6, 2, 1, 1]
#
#     numberMap = {}
#
#     max = len(arr)
#     for i in arr:
#         if not i in numberMap:
#             numberMap[i] = True
#
#         else:
#             print("Repeating =", i)
#
#     for i in range(1, max + 1):
#         if not i in numberMap:
#             print("Missing =", i)
#
#
#
# main()


# Method 1 (Use Sorting)
# Approach:
#
# Sort the input array.
# Traverse the array and check for missing and repeating.


def main():
    arr = [4, 3, 6, 2, 1, 1]

    sortedArr = sorted(arr)

    for i in range(1, len(arr)):
        if not i in sortedArr:
            print('missing', i)
        if sortedArr[i - 1] == sortedArr[i]:
            print("Repeated", i)


main()
