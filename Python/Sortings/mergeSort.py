def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        print(mid)
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge(left_arr)
        merge(right_arr)

        i = 0  # left arr
        j = 0  # right arr
        k = 0  # main arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


arr_test = [2, 4, 7, 5, 6, 1, 9, 3, 8]


print(merge(arr_test))
