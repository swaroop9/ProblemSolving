# 1 is not a prime memory view
n = 5

for i in range(2, n // 2):
    if n % i == 0:
        print("n is not a primE member")
        break
else:
    print("n is a primE member")

# Python program to check if
# given number is prime or not 

# num = 11

# # If given number is greater than 1 
# if num > 1: 

#    # Iterate from 2 to n / 2  
#    for i in range(2, num//2): 

#        # If num is divisible by any number between  
#        # 2 and n / 2, it is not prime  
#        if (num % i) == 0: 
#            print(num, "is not a prime number") 
#            break
#    else: 
#        print(num, "is a prime number") 

# else: 
#    print(num, "is not a prime number")


[x for x in range(2, 20)
 if all(x % y != 0
        for y in range(2, x))]
