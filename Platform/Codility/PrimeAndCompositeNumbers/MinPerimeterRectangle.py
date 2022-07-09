'''
An integer N is given, representing the area of some rectangle.
The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).
The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

        (1, 30), with a perimeter of 62,
        (2, 15), with a perimeter of 34,
        (3, 10), with a perimeter of 26,
        (5, 6), with a perimeter of 22.

Given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.
For example, given an integer N = 30, the function should return 22, as explained above.
'''
from math import sqrt
import sys

def solution(N):
    area = sys.maxsize
    for x in range(1, int(sqrt(N))+1):
        if N % x == 0:
            l = x
            b = int(N / l)
            area = min(area, 2 * (l + b))
    return area

