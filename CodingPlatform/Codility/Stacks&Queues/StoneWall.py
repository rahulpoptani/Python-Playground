'''
The only article that explain this question better 
https://www.programmersought.com/article/12395918889/
http://straightdeveloper.com/how-to-get-100-score-on-the-stonewall-exercise-on-codility/
'''


def solution(A):
    stack = []
    blocks = 0

    for x in A:
        while stack and stack[-1] > x:
            stack.pop()
        print(f"1. x: {x} stack: {stack}: blocks: {blocks}")
        if not stack or stack[-1] != x:
            stack.append(x)
            blocks += 1
        print(f"2. x: {x} stack: {stack}: blocks: {blocks}")
    return blocks

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))

