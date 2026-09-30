'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''

from Common.Tags import SIMULATION
from collections import defaultdict

def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])

    diagonals = defaultdict(list)

    for i in range(m):
        for j in range(n):
            diagonals[i + j].append(mat[i][j])

    result = []

    for i in range(m + n - 1):
        if i % 2 == 0:
            diagonals[i].reverse()
        result.extend(diagonals[i])

    return result

# Example usage:
print(findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
    