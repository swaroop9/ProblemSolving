Given
a
list
of
strings
arr, find if arr[i] is a
palindrome or not?

Input = ['hello', 'civic', 'mom', 'car', 'racecar', aabb]
Output = [False, True, True, False, True]

{'hello': False, 'civic': True, 'mom': True, 'car': False, 'racecar': True}
output = dict()


def palindrome(Input):
    output = []
    palindrome = False
    for value in Input:
        length = int(len(value))
        for i in range(0, int(length / 2)):
            if value[i] != value[length - i - 1]:
                palindrome = False
                break
        palindrom = True
    output.append(palindrom)
    return output


print(palindrome(Input))

temp_dict = {}
for char in value:
    if char in temp_dict:
temp_dict[char] += 1
else:
temp_dict[char] = 1
counnt = 0
for key in temp_dict:
    if temp_dict[key] % 2 != 0:
        count += 1
if count == 1:
    output.append(True)
else:
    output.append(False)

    # Given an array arr, Write a program to find the second largest element.
# Example:
# Input:
# arr = [65,34,9,23,99,27,56,76]
# Output:
# 76

arr = [65, 34, 9, 23, 99, 27, 56, 76]

# One way
arr.sort()
print(arr[-2])

# Other way
# Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
            mx != list1[i]:
        secondmax = list1[i]

print("Second highest number is : ", \
      str(secondmax))





