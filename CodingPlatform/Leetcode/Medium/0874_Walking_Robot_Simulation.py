'''
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:
-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note:
There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
 

Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation:
    The robot starts at (0, 0):
    Move north 4 units to (0, 4).
    Turn right.
    Move east 3 units to (3, 4).
    The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation:
    The robot starts at (0, 0):
    Move north 4 units to (0, 4).
    Turn right.
    Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
    Turn left.
    Move north 4 units to (1, 8).
    The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.

Example 3:
Input: commands = [6,-1,-1,6], obstacles = [[0,0]]
Output: 36
Explanation:
    The robot starts at (0, 0):
    Move north 6 units to (0, 6).
    Turn right.
    Turn right.
    Move south 5 units and get blocked by the obstacle at (0,0), robot is at (0, 1).
    The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.
'''

from Common.Tags import SIMULATION

def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    # Directions: North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction_index = 0
    max_distance_squared = 0
    obstacle_set = set(map(tuple, obstacles))

    for command in commands:
        if command == -2:  # Turn left
            direction_index = (direction_index - 1) % 4
        elif command == -1:  # Turn right
            direction_index = (direction_index + 1) % 4
        else:  # Move forward command units
            dx, dy = directions[direction_index]
            for _ in range(command):
                if (x + dx, y + dy) not in obstacle_set:
                    x += dx
                    y += dy
                    max_distance_squared = max(max_distance_squared, x * x + y * y)
                else:
                    break

    return max_distance_squared

# Example usage:
print(robotSim([4, -1, 3], []))  # Output: 25
print(robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # Output: 65
print(robotSim([6, -1, -1, 6], [[0, 0]]))  # Output: 36