'''Method#1: Brute Force solution ; Time and Space = 0(n**2) & O(1)'''
def findPair_1(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) == k:
                return True
    return False
            

'''Method#2: Sorting and two pointers; Time and Space = based on sorting algo & O(nlogn)'''
def findPair_2(arr, k):
    arr.sort()
    left = 0
    right = len(arr)-1
    while(left < right):
        if arr[left] + arr[right] == k:
            return True
        elif arr[left] + arr[right] > k:
            right-=1
        else:
            left+=1
    return False


''' Method#3: Using Hash Table(Dict); Time and Space = O(n) & O(n)'''
def findPair_3(arr, k):
    visited = {}
    for ele in arr:
        if visited.get(k - ele):
            return True
        else:
            visited[ele] = True
    return False

arr = [4, 5, 1, -3, 6]
k = -2
print(f"Method_1 : {findPair_1(arr, k)}")
print(f"Method_2 : {findPair_2(arr, k)}")
print(f"Method_3 : {findPair_3(arr, k)}")