# Determine whether a triangle can be built from a given set of edges.
# A triplet (P, Q, R) is triangular if 0 <= P < Q < R < N and:
#         A[P] + A[Q] > A[R],
#         A[Q] + A[R] > A[P],
#         A[R] + A[P] > A[Q].

def solution(A):
    def isTriangle(P, Q, R):
        return (P+Q>R) and (Q+R>P) and (R+P>Q)
    
    A.sort()

    for x in range(len(A)-2):
        if isTriangle(A[x], A[x+1], A[x+2]):
            return 1
    return 0

print(solution([10, 2, 5, 1, 8, 20]))