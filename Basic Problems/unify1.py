'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


# Write your code here

tcs = int(input())

x = input()
lx = x.split()

y = 0
while y < tcs:
    for i in range(1, int(lx[y]) + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0:
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        print(i)
    y += 1

    # Input
    # 2
    # 3 15
