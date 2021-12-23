# levels = [5, 1, 3, 2, 3, 4, 6, 7, 9, 3, 1, 2]
levels = [1, 3, 2, 0, 5, 2, 5, 4, 1, 2]

maxCapacity = 0
# Time : O(n^2) // Space o(n)
for i in range(len(levels)):
    for j in range(i + 1, len(levels)):
        maxValue = min(levels[j], levels[i]) * (j - i)
        maxCapacity = max(maxValue, maxCapacity)

print(maxCapacity)

# Time : o(n) // Space(n)
left = 0
right = len(levels) - 1
while left < right:
    maxValue = min(levels[left], levels[right]) * (right - left)
    maxCapacity = max(maxValue, maxCapacity)
    if levels[left] < levels[right]:
        left += 1
    else:
        right -= 1

print(maxCapacity)
