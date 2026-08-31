'''
You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.
'''
from Common.Tags import MATRIX, SET, SIMULATION

def queensAttack(n, k, r_q, c_q, obstacles):
    # Create a set of obstacles for O(1) lookups
    obstacle_set = set((r, c) for r, c in obstacles)
    
    # Directions the queen can move: vertical, horizontal, and diagonal
    directions = [
        (1, 0),   # up
        (-1, 0),  # down
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # up-right
        (1, -1),  # up-left
        (-1, 1),  # down-right
        (-1, -1)  # down-left
    ]
    
    attackable_squares = 0
    
    for dr, dc in directions:
        r, c = r_q + dr, c_q + dc
        
        while 1 <= r <= n and 1 <= c <= n:
            if (r, c) in obstacle_set:
                break
            attackable_squares += 1
            r += dr
            c += dc
            
    return attackable_squares

print(queensAttack(5, 3, 4, 3, [(5, 5), (4, 2), (2, 3)]))  # Example usage