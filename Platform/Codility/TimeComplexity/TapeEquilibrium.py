'''
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:
        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7
the function should return 1
'''

import sys

def solution(A):
    result = sys.maxsize
    leftSum = rightSum = 0
    for x in A: 
        rightSum += x
    for x in range(len(A)-1):
        leftSum += A[x]
        rightSum -= A[x]
        result = min(result, abs(leftSum - rightSum))
    return result

print(solution([3, 1, 2, 4, 3]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1]))
print(solution([1, 2]))
print(solution([-1, -2, 2]))
print(solution([0, 0, 0, 0]))
print(solution([1000, -1000]))
    



