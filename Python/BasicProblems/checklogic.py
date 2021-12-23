# for i in range(10 - 1, 1, -1):  # fix a
#     print(i)
l = [1, 2, 3, 4, 5, 6, 7]
n = 7
for i in range(n - 1, 1, -1):
    l[i]
    left = 0
    right = n - 2

    print(i, l[i], left, right, l[right])
