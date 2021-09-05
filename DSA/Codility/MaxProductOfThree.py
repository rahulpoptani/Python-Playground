# For example, array A such that:
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6

# contains the following example triplets:

#         (0, 1, 2), product is −3 * 1 * 2 = −6
#         (1, 2, 4), product is 1 * 2 * 5 = 10
#         (2, 4, 5), product is 2 * 5 * 6 = 60

# Your goal is to find the maximal product of any triplet. Dont consider sequence

def solution(A):
    A.sort()
    if A[0] < 0 and A[1] < 0 and A[-1] > 0:
        return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
    else:
        return A[-3] * A[-2] * A[-1]

print(solution([4,5,2,-6,1,1,1,-100]))