def is_Power_of_three(n):
    while n % 3 == 0:
        # print(n)
        n /= 3
    return n == 1


print(is_Power_of_three(243))


# print(is_Power_of_three(81))
# print(is_Power_of_three(21))


def is_Power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


print(is_Power_of_two(4))
print(is_Power_of_two(36))
print(is_Power_of_two(16))
