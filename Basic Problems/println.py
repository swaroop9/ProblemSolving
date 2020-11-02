x = list(input())
print(type(x))
print(x)
l = []
for i in x:
    if i != " ":
        # print(i)
        l.append(i)

print(*l)

# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line

print("geeks", end = " ")
print("geeksforgeeks")

# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in range(4):
	print(a[i], end =" ")
