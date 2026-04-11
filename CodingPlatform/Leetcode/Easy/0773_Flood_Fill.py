'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and 
shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
'''
from Common.Tags import GRIND_75, MATRIX, BFS

from typing import List
from collections import deque

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]

    if start_color == color:
        return image

    rows, cols = len(image), len(image[0])
    queue = deque()
    queue.append((sr, sc))
    image[sr][sc] = color

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == start_color:
                image[nx][ny] = color
                queue.append((nx, ny))

    return image


print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(floodFill([[1,1,0]], 0, 0, 2))
