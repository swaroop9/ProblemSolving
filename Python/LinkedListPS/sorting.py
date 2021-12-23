arr = [1, 2, 9, 10, 4, 8, 5, 3, 6, 7]

# https://stackabuse.com/sorting-algorithms-in-python/

length = len(arr)

# for i in range(length):
#     for j in range(length):
#         if arr[i] < arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#
# print(arr)


mx = max(arr[0], arr[1])
second_highest = min(arr[0], arr[1])

for i in range(2, length):
    if arr[i] > mx:
        second_highest = mx
        mx = arr[i]
    elif second_highest < arr[i] and mx != arr[i]:
        second_highest = arr[i]

print(second_highest)
