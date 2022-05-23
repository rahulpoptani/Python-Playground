import os,sys
sys.path.append(os.curdir)
from DataStructures.Stack.Stack import Stack

def balance_parenthesis(data):
    stack = Stack()
    for x in data:
        if x == '(' or x == '{' or x == '[':
            stack.push(x)
        elif stack and x == ')' and stack.peek() == '(':
            stack.pop()
        elif stack and x == '}' and stack.peek() == '{':
            stack.pop()
        elif stack and x == ']' and stack.peek() == '[':
            stack.pop()
        else:
            return False
    if len(stack.list) > 0: return False
    return True

print(balance_parenthesis('({}([]))'))

