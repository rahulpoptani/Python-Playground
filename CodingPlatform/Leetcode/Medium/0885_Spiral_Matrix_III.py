'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:
    Input: rows = 1, cols = 4, rStart = 0, cStart = 0
    Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:
    Input: rows = 5, cols = 6, rStart = 1, cStart = 4
    Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
'''

from Common.Tags import SIMULATION, MATRIX

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
    directions = [
            (0, 1),    # East
            (1, 0),    # South
            (0, -1),   # West
            (-1, 0)    # North
    ]

    result = [[rStart, cStart]]

    r, c = rStart, cStart

    step = 1
    direction = 0

    while len(result) < rows * cols:

        # Same step length for 2 directions
        for _ in range(2):

            dr, dc = directions[direction]

            for _ in range(step):
                r += dr
                c += dc

                # Add only if inside the matrix
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

            direction = (direction + 1) % 4

        step += 1

    return result

# Example usage:
print(spiralMatrixIII(1, 4, 0, 0))  # Output: [[0,0],[0,1],[0,2],[0,3]]
print(spiralMatrixIII(5, 6, 1, 4))  # Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]