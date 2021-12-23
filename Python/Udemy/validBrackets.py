'''Method#1: Brute Force solution; Time and Space = 0(n) & O(n)'''
def validBrackets_1(brackets):
    openBrackets = ['{', '(', '[']
    bracketMatch = {'}':'{', ']':'[', ')':'('}
    stack = []
    for bracket in brackets:
        if bracket in openBrackets:
            stack.append(bracket)
        elif (len(stack)>0 and bracketMatch[bracket] == stack[-1]):
            stack.pop()
        else:
            return False
    return len(stack) == 0


brackets = "{({[{}]})}"
print(validBrackets_1(brackets))