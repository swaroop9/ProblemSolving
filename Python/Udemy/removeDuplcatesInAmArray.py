'''Method#1: Brute Force solution; Time and Space = 0(n*2) & O(n)'''
def removeDuplicates_1(arr):
    noDuplicatesArray = []
    for ele in arr:
        if ele not in noDuplicatesArray:
            noDuplicatesArray.append(ele)
    return noDuplicatesArray


'''Method#2: using sort ; Time and Space = 0(nlogn) & O(n)'''
def removeDuplicates_2(arr):
    if len(arr) == 0:
        return []
    noDuplicatesArray =[arr[0]]
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            noDuplicatesArray.append(arr[i])
    return noDuplicatesArray


'''Method#3: Hash Table or dict ; Time and Space = 0(n) & O(n)'''
def removeDuplicates_3(arr):
    if len(arr) == 0:
        return []
    noDuplicates = {}
    for ele in arr:
        noDuplicates[ele] = True 
    noDuplicatesArray = list(noDuplicates.keys())
    
    return noDuplicatesArray


arr = [1, 2, 2, 3, 4, 1, 5, 2, 4]
print(removeDuplicates_1(arr))
print(removeDuplicates_2(arr))
print(removeDuplicates_3(arr))