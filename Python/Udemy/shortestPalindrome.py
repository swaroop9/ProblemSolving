'''Method#1: Brute Force solution; Time and Space = 0(n**2) & O(1)'''
def shortestPalindrome(str):
    mirrorLength = 0
    for i in range(len(str)):
        if str[:i] == str[:i][::-1]:
            mirrorLength=i
    return str[mirrorLength:][::-1] + str


str  ='acbcabcbb'
print(shortestPalindrome(str))