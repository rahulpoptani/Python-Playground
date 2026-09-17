'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
'''

from Common.Tags import SIMULATION, MATRIX

def generateMatrix(n: int) -> list[list[int]]:
    if n <= 0:
        return []
    
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
    return matrix

# Example usage:
print(generateMatrix(3))  # Output: [[1,2,3],[8,9,4],[7,6,5]]
print(generateMatrix(1))  # Output: [[1]]
print(generateMatrix(4))  # Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]