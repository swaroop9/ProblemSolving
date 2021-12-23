


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        # print(i)
        key = arr[i] # 3
        j = i-1 #0 ,6
        while ((j >= 0) and (key < arr[j])):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr
        




arr = [6, 3, 4, 5, 8, 1, 2]

print(insertion_sort(arr))