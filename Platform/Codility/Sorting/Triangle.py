'''
Determine whether a triangle can be built from a given set of edges.
A triplet (P, Q, R) is triangular if 0 <= P < Q < R < N and:
        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.
returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

A[0] = 10    A[1] = 50    A[2] = 5
A[3] = 1

the function should return 0.
'''

def solution(A):
    def isTriangle(P, Q, R):
        return (P+Q>R) and (Q+R>P) and (R+P>Q)
    
    A.sort()

    for x in range(len(A)-2):
        if isTriangle(A[x], A[x+1], A[x+2]):
            return 1
    return 0

print(solution([10, 2, 5, 1, 8, 20]))
print(solution([10, 50, 5, 1]))
print(solution([10, 50, 1]))
print(solution([10, 50]))

