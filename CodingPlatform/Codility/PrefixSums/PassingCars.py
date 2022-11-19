'''
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
Array A contains only 0s and/or 1s:
        0 represents a car traveling east,
        1 represents a car traveling west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4). The function should return 5, as explained above.
The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000
'''

def solution(A):
    east = west = 0
    for x in A:
        if x == 0:
            east += 1
        else:
            west += east
            if west > 1000000000: return -1
    return west

print(solution([0, 1, 0, 1, 1]))
print(solution([0]))
print(solution([1]))
print(solution([0, 1]))
print(solution([1, 1]))
print(solution([1, 0]))