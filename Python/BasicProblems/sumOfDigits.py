def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit():
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))


# Python3 program to calculate sum of
# all numbers present in a str1ing
# containing alphanumeric characters

# Function to calculate sum of all
# numbers present in a str1ing
# containing alphanumeric characters
def findSum(str1):
    # A temporary str1ing
    temp = ""

    # holds sum of all numbers
    # present in the str1ing
    Sum = 0

    # read each character in input string
    for ch in str1:

        # if current character is a digit
        if ch.isdigit():
            temp += ch

        # if current character is an alphabet
        else:

            # increment Sum by number found
            # earlier(if any)
            Sum += int(temp)

            # reset temporary str1ing to empty
            temp = "0"

    # atoi(temp.c_str1()) takes care
    # of trailing numbers
    return Sum + int(temp)


# Driver code

# input alphanumeric str1ing
str1 = "12abc20yz68"

print(findSum(str1))

# This code is contributed
# by mohit kumar


# Python3 program to calculate sum of
# all numbers present in a str1ing
# containing alphanumeric characters

# Function to calculate sum of all
# numbers present in a str1ing
# containing alphanumeric characters


import re


def find_sum(str1):
    # Regular Expression that matches digits in between a string
    return sum(map(int, re.findall('\d+', str1)))


# Driver code

# input alphanumeric str1ing
str1 = "12abc20yz68"

print(find_sum(str1))

