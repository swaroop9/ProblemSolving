# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fib(n - 1) + fib(n - 2)


"""It takes lot of time if n is big due to recurssion"""

# memoization: IDea: Cache values
# Implement explicitly
fib_cache = {}


def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)

    fib_cache[n] = value
    # print(fib_cache)
    return value


# use buildin python tool (least recently used cache)
# from functools import lru_cache

# @lru_cache(maxsize=1000)
# def fib(n):
#     if type(n)==int:
#         raise TypeError("N must be an positive intergar")
#     if n<1:
#         raise ValueError("N must be an positive intergar")
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>2:
#         return fib(n-1)+fib(n-2)


# n = int(input("Enter the fibanocci value of n"))

# print('fibanocci value of n is:', fib(n))

for i in range(1, 11):
    print(fib(i))
