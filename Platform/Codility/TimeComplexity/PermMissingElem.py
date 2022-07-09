'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
'''

def solution(A):
    first_element = 1
    last_element = len(A)+1
    sum_ofall_element = (last_element * (last_element + first_element)) / 2
    for x in A:
        sum_ofall_element = sum_ofall_element - x
    return int(sum_ofall_element)

print(solution([2, 3, 1, 5]))
print(solution([1, 2, 3, 4]))
print(solution([]))

