# The next greater element is the first element towards the right which is greater than the given element
# Input: list = [4, 6, 3, 2, 8, 1]
# Output: result = [6, 8, 8, 8, -1, -1]

from Stack import Stack
from typing import List
import sys

# Brute Force O(n square)
def next_greatest_element(lst:List):
    result = []
    for x in range(0,len(lst)):
        next_greatest = -1
        for y in range(x+1, len(lst)):
            if lst[y] > lst[x]:
                next_greatest = lst[y] 
                break
        result.append(next_greatest)
    print(result)

# next_greatest_element([4, 6, 3, 2, 8, 1])


# Using Stack O(n)
def next_greater_element(lst):
    stack = Stack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        print(f'Processing Element: {lst[i]}')
        # While stack has elements and current element is greater than top element, pop all elements
        while not stack.isEmpty and stack.peek() <= lst[i]:
            print(f'Stack is not Empty and Current Peak: {stack.peek()} is Less than Current Element: {lst[i]}. Poping Element: {stack.pop()}')
        # If stack has an element, top element will be greater than ith element
        if not stack.isEmpty:
            res[i] = stack.peek()
            print(f'Adding last element: {stack.peek()} in result: {res}')
        # push in the current element in stack
        stack.push(lst[i])
        print(f'Pushed: {lst[i]} in Stack: {stack}')
    print(res)

next_greater_element([4, 6, 3, 2, 8, 1])
