'''
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.

Example
For items = [3, 5, 2, 4, 5], the output should be
solution(items) = [-1, 3, -1, 2, 4].
'''

def solution(items):
    # Using stack for O(n) time complexity
    result = []
    stack = []  # Monotonic stack to keep track of elements
    
    for item in items:
        # Remove elements from stack that are >= current item
        while stack and stack[-1] >= item:
            stack.pop()
        
        # If stack is not empty, top element is the closest smaller element
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        
        # Push current element to stack
        stack.append(item)
    
    return result

print(solution(items=[3, 5, 2, 4, 5]))
