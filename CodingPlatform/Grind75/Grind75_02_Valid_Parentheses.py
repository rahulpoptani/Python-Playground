'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''

def isValid(s: str) -> bool:
    stack = []
    openParanthesis = ['(', '{', '[']
    closeParanthesis = [')', '}', ']']
    for c in s:
        if c in openParanthesis:
            stack.append(c)
        else:
            try:
                e = stack.pop()
                if c in closeParanthesis:
                    if c == ')' and not e == '(': return False
                    elif c == '}' and not e == '{': return False
                    elif c == ']' and not e == '[': return False
                else: return False
            except IndexError: return False
    if stack: return False
    return True

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("["))
print(isValid("]"))
print(isValid("(-"))