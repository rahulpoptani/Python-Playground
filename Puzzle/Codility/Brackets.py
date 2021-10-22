# Check the string with brackets are valid using Stacks

def valid_brackets(s):
    valid = True
    stack = []
    for c in s:
        if c == '{' or c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            valid = False if not stack or stack.pop() != '(' else valid
        elif c == ']':
            valid = False if not stack or stack.pop() != '[' else valid
        elif c == '}':
            valid = False if not stack or stack.pop() != '{' else valid
    return 1 if valid and not stack else 0

print(valid_brackets('[(())]'))
