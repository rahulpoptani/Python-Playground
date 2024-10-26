'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
'''

from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]
    visit = set()
    queue = [(sr,sc)]
    while queue:
        current = queue.pop()
        visit.add(current)
        image[current[0]][current[1]] = color

        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            newX, newY = current[0] + x, current[1] + y
            if (newX, newY) not in visit and newX >= 0 and newY >= 0 and newX < len(image) and newY < len(image[0]) and image[newX][newY] == start_color:
                queue.insert(0, (newX, newY))        
    return image


print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(floodFill([[1,1,0]], 0, 0, 2))
