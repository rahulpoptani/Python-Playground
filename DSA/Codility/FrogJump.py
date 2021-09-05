# From X to Y, a frog can jump D distance, Number of Jump required to jump at or beyond Y from X
# Ex: X = 10, Y = 85, D = 30
# 1st Jump = 10 + 30 = 40
# 2nd Jump = 10 + 30 + 30 = 70
# 3rd Jump = 10 + 30 + 30 + 30 = 100
# Total Jump = 3
import math

def solution(X, Y, D):
    jump = 0
    while X < Y:
        X = X + D
        jump += 1
    print(jump)

solution(10, 85, 30)

def frogJump(x, y, d):
    print (math.ceil((y-x)/d))

frogJump(10, 85, 30)