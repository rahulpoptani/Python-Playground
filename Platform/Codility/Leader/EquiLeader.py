'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

the function should return 2, as explained above.
Given a non-empty array A consisting of N integers, returns the number of equi leaders.
'''

# LOGIC CHANGED

def solution(A):
    freq = {}
    for x in A:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    
    if freq:
        leader, occurence = max(freq.items(), key=lambda x: x[1])
    else:
        return 0
    
    equiLeaderCount = 0
    leadersInLeft = 0
    leadersInRight = occurence
    elementsLeftSide = 0
    elementsRightSide = len(A)

    for x in A:
        if x == leader:
            leadersInRight -= 1
            leadersInLeft += 1
        elementsRightSide -= 1
        elementsLeftSide += 1
        if (leadersInLeft > elementsLeftSide // 2) and (leadersInRight > elementsRightSide // 2):
            equiLeaderCount += 1
    
    return equiLeaderCount
    

print(solution([4, 3, 4, 4, 4, 2]))
print(solution([]))
