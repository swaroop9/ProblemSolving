"""Method One"""

# n=5
# fact=1

# if n>0 and type(n)==int:
#     for i in range(1,n+1):
#         if(n==0 or n==1):
#             fact = 1
#         else:
#             fact*=i
#     print(fact)

# else:
#     raise ValueError("Input must be positive integer")


"""Method two"""

n = 5


def fact(n):
    if n > 0 and type(n) == int:
        if n == 0 or n == 1:
            return 1
        else:
            return n * fact(n - 1)
    else:
        raise ValueError("Input must be positive integer")


print(fact(5))
