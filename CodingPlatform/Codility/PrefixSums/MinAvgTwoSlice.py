'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A 
(notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

the function should return 1, as explained above.

The goal is to find the starting position of a slice whose average is minimal.
If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

'''
import sys

def solution(A):
    index2 = index3 = -1
    minSum2 = minSum3 = sys.maxsize

    for x in range(len(A)-1):
        val1 = A[x]
        val2 = A[x+1]
        sum2 = val1 + val2
        if (sum2 < minSum2):
            minSum2 = sum2
            index2 = x
        
        if (x < len(A)-2):
            val3 = A[x+2]
            sum3 = val1 + val2 + val3
            if sum3 < minSum3:
                minSum3 = sum3
                index3 = x
    
    if (index3 == -1):
        return index2
    
    minSum2 = minSum2 / 2
    minSum3 = minSum3 / 3
    if (minSum2 < minSum3): return index2
    if (minSum3 < minSum2): return index3
    
    return min(index2, index3) # if both minSum2 and minSum3 are same then return minimum

print(solution([4, 2, 2, 5, 1, 5, 8]))
print(solution([4, 2]))
print(solution([10, 11, -20, 5]))