'''Method#1: Brute Force solution ; Time and Space = 0(n*2) & O(n)'''
def findDuplicates_1(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[j]


'''Method#2: using sort ; Time and Space = 0(nlogn) & O(n)'''
def findDuplicates_2(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return arr[i]



'''Method#3: Hash Table or dict ; Time and Space = 0(n) & O(n)'''
def findDuplicates_3(arr):
    visited = {}
    for ele in arr:
        if visited.get(ele):
            return ele
        else:
            visited[ele] = True 

# Tortoise and harse

arr = [1, 2, 3, 4, 5, 6, 3, 7]
print(findDuplicates_1(arr))
print(findDuplicates_2(arr))
print(findDuplicates_3(arr))