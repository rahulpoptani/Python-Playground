'''
A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
For example, given:
  X = 10
  Y = 85
  D = 30
'''
import math
def solution(X, Y, D):
    return math.ceil((Y-X)/D)

print(solution(10, 85, 30))
print(solution(10, 10, 1))
    