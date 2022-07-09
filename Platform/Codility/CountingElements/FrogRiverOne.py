'''
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves).

For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
'''

def solution(X, A):
    myset = set()
    for x in range(1, X+1):
        myset.add(x)
    for x in range(len(A)):
        try:
            myset.remove(A[x])
        except KeyError:
            pass
        if len(myset) == 0:
            return x
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(5, [1, 3, 1, 4, 3, 5, 4, 2, 5]))
print(solution(5, [1]))