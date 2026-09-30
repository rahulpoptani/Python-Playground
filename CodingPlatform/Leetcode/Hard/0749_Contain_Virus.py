'''
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.
The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.
Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.
Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.

Example 1:
Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:
Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

Example 3:
Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
'''

from Common.Tags import SIMULATION
from typing import List

def containVirus(isInfected: List[List[int]]) -> int:

    m = len(isInfected)
    n = len(isInfected[0])

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    total_walls = 0

    while True:

        visited = [[False] * n for _ in range(m)]

        regions = []
        threatened = []
        walls = []

        # 1. Find all infected regions
        for r in range(m):
            for c in range(n):

                if isInfected[r][c] != 1 or visited[r][c]:
                    continue

                region = []
                danger = set()
                wall_count = 0

                stack = [(r, c)]
                visited[r][c] = True

                while stack:

                    x, y = stack.pop()

                    region.append((x, y))

                    for dx, dy in directions:

                        nx = x + dx
                        ny = y + dy

                        # Outside grid
                        if not (0 <= nx < m and 0 <= ny < n):
                            continue

                        # Healthy cell
                        if isInfected[nx][ny] == 0:
                            danger.add((nx, ny))
                            wall_count += 1

                        # Another infected cell
                        elif (
                            isInfected[nx][ny] == 1
                            and not visited[nx][ny]
                        ):
                            visited[nx][ny] = True
                            stack.append((nx, ny))

                regions.append(region)
                threatened.append(danger)
                walls.append(wall_count)

        # No active regions
        if not regions:
            break

        # 2. Find the most dangerous region
        most_dangerous = max(
            range(len(regions)),
            key=lambda i: len(threatened[i])
        )

        # If nobody can infect anything,
        # we are done.
        if len(threatened[most_dangerous]) == 0:
            break

        # 3. Build walls around that region
        total_walls += walls[most_dangerous]

        # Mark it as quarantined
        for r, c in regions[most_dangerous]:
            isInfected[r][c] = -1

        # 4. Let all other regions spread
        for i in range(len(regions)):

            if i == most_dangerous:
                continue

            for r, c in threatened[i]:
                isInfected[r][c] = 1

    return total_walls

# Example usage:
print(containVirus([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]))  # Output: 10
print(containVirus([[1,1,1],[1,0,1],[1,1,1]]))  # Output: 4
print(containVirus([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]))  # Output: 13