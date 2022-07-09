'''
Robot Return to origin
There is a robot starting at the position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. 
Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Input: moves = "UD"
Output: true

Input: moves = "LL"
Output: false
'''

# INCORRECT! Not handling corner case


def judgeCircle(moves: str) -> bool:
    x = y = 0
    head = moves[0]
    for m in moves:
        head = m
        if m == 'U': 
            if head == 'U': x += 1
            else: x -= 1
        elif m == 'D': 
            if head == 'D':x -= 1
            else: x += 1
        elif m == 'R': 
            if head == 'R': x += 1
            else: x -= 1
        elif m == 'L': 
            if head == 'L': x -= 1
            else: x += 1
        print(x,y)
    return x == 0 and y == 0
        



# print(judgeCircle('UD'))
# print(judgeCircle('LL'))
print(judgeCircle('LLLL'))

