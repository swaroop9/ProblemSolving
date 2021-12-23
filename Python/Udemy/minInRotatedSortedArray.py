'''Method#1: Brute Force solution ; Time and Space = 0(n) & O(1)'''
def findMinInRotatedSortedArray_1(arr):
    min = arr[0]
    for ele in arr:
        if min > ele:
            min = ele
    return min

'''Method#2: Divide and Concur; Time and Space = 0(logn) & O(1)'''
def findMinInRotatedSortedArray_2(arr):
    left = 0
    right = len(arr)-1
    if arr[right] > arr[left]: return arr[left]
    while(left<right):
        mid = left + (right - left)//2
        if arr[mid] > arr [mid + 1]:
            return arr[mid+1]
        elif arr[mid] < arr[mid - 1]:
            return arr[mid]
        elif arr[mid] > arr[right]:
            left=mid+1
        else:
            right=mid-1
    return arr[left]


arr = [4, 5, 6, 7, -1, 1, 2, 3, 3]
print(findMinInRotatedSortedArray_1(arr))
print(findMinInRotatedSortedArray_2(arr))