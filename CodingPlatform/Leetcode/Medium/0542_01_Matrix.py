'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two cells sharing a common edge is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''

from Common.Tags import BFS, MATRIX
from collections import deque
from typing import List

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    rows, cols = len(mat), len(mat[0])
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = float('inf')
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            row, col = r + dr, c + dc
            if 0 <= row < rows and 0 <= col < cols and mat[row][col] == float('inf'):
                mat[row][col] = mat[r][c] + 1
                queue.append((row, col))
    return mat

# Test cases
print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1]]