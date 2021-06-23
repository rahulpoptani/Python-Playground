# The figure below shows discs drawn for N = 6 and A as follows:
#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0
# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# There are eleven (unordered) pairs of discs that intersect, namely:
# - discs 1 and 4 intersect, and both intersect with all the other discs;
# - disc 2 also intersects with discs 0 and 3.

def solution(arr):
    open = [None] * len(arr)
    close = [None] * len(arr)
    intersect = 0
    for x in range(len(arr)):
        open[x] = x - arr[x]
        close[x] = x + arr[x]
    
    print(open)
    print(close)

    for x in range(len(arr)):
        for y in range(open[x], close[x]+1):
            intersect += open.count(y)
        intersect -= 1
    
    print(intersect-1)


solution([1, 5, 2, 1, 4, 0])
