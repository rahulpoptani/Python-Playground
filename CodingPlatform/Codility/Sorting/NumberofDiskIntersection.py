'''
We draw N discs on a plane. The discs are numbered from 0 to N − 1. 
An array A of N non-negative integers, specifying the radiuses of the discs, is given. 
The J-th disc is drawn with its center at (J, 0) and radius A[J].
We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0
https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

There are eleven (unordered) pairs of discs that intersect, namely:
        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.


'''

from opcode import opname


def solution(A):
    size = len(A)
    open = [None] * size
    close = [None] * size
    intersect = 0
    for x in range(size):
        open[x] = x - A[x]
        close[x] = x + A[x]
    
    # print(open)
    # print(close)

    for x in range(len(A)):
        for y in range(open[x], close[x]+1):
            if open[x] == close[x]: continue
            intersect += open.count(y)
        intersect -= 1
        # print(f'open: {open[x]} close: {close[x]} int: {intersect}')
    
    if (intersect -1 > 10000000): return -1
    else: return intersect


print(solution([1, 5, 2, 1, 4, 0]))
print(solution([]))
print(solution([0, 1]))

