def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        minPos = i
        for j in range(i+1,n):
            if (arr[j] < arr[minPos]):
                minPos = j
        arr[i], arr[minPos] = arr[minPos], arr[i]
        print(arr)
    return arr

arr = [6, 3, 4, 5, 8, 1, 2]

print(selection_sort(arr))



# Selection sort in Python

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # To sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)