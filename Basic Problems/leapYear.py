# n = int(input("Enter N value"))

# if n%2 != 0:
#     print("ODD")
#     print("N is odd")
# else:
#      print("Even")


# for i in range(0,n):
#     print(i**2)

# if __name__ == '__main__':
#     n = int(input())


def is_leap(year):
    # leap = False
    # if (year%4 ==0 and year %100 ==0 and year % 400 ==0):
    #     leap = True
    return year % 4 == 0 and (year % 100 != 0 and year % 400 == 0)


year = int(input())
if is_leap(year):
    print("is_leap(year)")
else:
    print("isNot_leap(year)")

import calendar

print(calendar.isleap(int(input("Enter Year"))))
