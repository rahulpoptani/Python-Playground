'''
List of expected revenues and payments in chronological order
The problem is that at some point of time the sum of previous payments can be more than total previous revenues.
Which would put company in debt at start of the year. To avoid reschedule the payment to end of year (array).

Given A = [10, -10, -1, -1, 10]. Number of relocations = 1. It's enough to move -10 to end of array
Given A = [-1, -1, -1, 1, 1, 1, 1]. Number of relocation = 3. 
Give A = [5, -2, -3, 1]. Number of relocations = 0. Balance is non negative throughout the year

Note: The sum of all in array is always positive
'''

from copy import copy
import heapq

def solutions(A):
    B = copy(A)
    heapq.heapify(B)
    sum = 0
    relocations = 0
    for x in A:
        sum += x
        # print(f'Sum Now: {sum}')
        if sum < 0:
            sum += heapq.heappop(B) * -1
            relocations += 1
            # print(f'Sum is low: adding from heap. new Sum: {sum}')
    return relocations

print(solutions([10, -10, -1, -1, 10]))
print(solutions([-1, -1, -1, 1, 1, 1, 1]))
print(solutions([5, -2, -3, 1]))


