"""Balanced parentheses are to check for a given string that contains parentheses (or brackets), should have equal opening and closing count as well as positionally well structured. For the context of this problem, we will use balanced parentheses as – ‘()’, ‘[]’, ‘{}’ – i.e given string can have any combination of these brackets.

Please note that before attempting the problem, it’s good to clarify if the string will just contain the bracket characters or any numbers, etc (as this might change the logic a bit)

Example: A given string – ‘{ [ ] {} ()} – is a balanced string as it’s structured and has equal no of closing and opening parentheses, but string – ‘{ [ } ] {} ()’ – this string – even though has equal no of opening and closing parentheses this is still not balanced because you can see that without a closing ‘[‘ we’ve closed ‘}’ (i.e. all inner brackets should be closed before closing an outer bracket)

We will be using a stack data structure to solve this problem. If you want to know more about basics of stack please refer here

A stack is a LIFO (Last In First Out type of data structure), think of it as a stack/pile of plates at a wedding – you will pick up the topmost plate whenever you are using it.

"""


# Python3 program to check  for
# balanced parenthesis.

# function to check if
# paranthesis are balanced

def areParanthesisBalanced(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    expr = "{()}[]}";
    if areParanthesisBalanced(expr):
        print("Balanced");
    else:
        print("Not Balanced");
