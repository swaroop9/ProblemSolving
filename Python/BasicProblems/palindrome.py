# n = 153
# number = n
# sum_n = 0
# while n != 0:
#     x = n % 10
#     sum_n += x ** 3
#     n = int(n / 10)
#     print(sum_n)
#
# if sum_n == number:
#     print("palindrome")
# else:
#     print("Not palindrome")


# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")


# function to check string is
# palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# Python program to check
# if a string is palindrome
# or not

x = "malayalm"

w = ""
for i in x:
    w = i + w

if x == w:
    print("Yes")
else:
    print("No")
