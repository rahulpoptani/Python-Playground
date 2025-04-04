'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Example 4:
Input: board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"
Output: true
'''

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word): return True

        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path): return False

        path.add((r, c))
        res = (dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1))
        path.remove((r,c))
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
    
    return False


print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
print(exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))