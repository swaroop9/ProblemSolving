'''Method#1: Brute Force algo; Space and Time :0(1) & O(n**2)'''
def firstRepeatingCharacter_1(str):
    for i in range(len(str)):
        for j in range(i):
            if str[i] == str[j]:
                return str[i]
    return '\0'

'''Method#2: Using Hash Table(Dict); Time and Space = O(n) & O(n)'''
def firstRepeatingCharacter_2(str):
    visited = {}
    for char in str:
        if visited.get(char):
            return char
        else:
            visited[char] = True
    return '\0'


'''Method#3:Using Hash Table(Dict); Space and Time :0(n) & O(n)'''
def firstRepeatingCharacter_3(str):
    di = {}

    for char in str:
        if di.get(char):
            di[char] += 1
        else:
            di[char] = 1

    for key in di.keys():
        if di[key] > 1:
            return key
    return '\0'

str = 'insidecode'
print(f"Method_1 : {firstRepeatingCharacter_1(str)}")
print(f"Method_2 : {firstRepeatingCharacter_2(str)}")
print(f"Method_3 : {firstRepeatingCharacter_3(str)}")
