# The only article that explain this question better 
# https://www.programmersought.com/article/12395918889/
# http://straightdeveloper.com/how-to-get-100-score-on-the-stonewall-exercise-on-codility/


def solution(arr):
    stack = []
    blocks = 0

    for x in arr:
        while stack and stack[-1] > x:
            stack.pop()
        
        if not stack or stack[-1] < x:
            stack.append(x)
            blocks += 1
    return blocks

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))

