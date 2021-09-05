# Leader is the one with highest frequency and frequency more than half size of array
# An equi leader is an index S such that 0 ≤ S < N − 1 
# and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] 
# have leaders of the same value.
# First find leader in array and then scan for same as equileader

def find_leader(arr):
    cons_size = 0
    cand = 0
    for x in arr:
        if cons_size == 0:
            cand = x
            cons_size += 1
        elif cand == x:
            cons_size += 1
        else:
            cons_size -= 1
    occurence = arr.count(cand)
    if occurence > (len(arr)/2):
        return arr.index(cand)
    else:
        return -1

print(find_leader([3,0,1,1,4,1,1]))

print(find_leader([4,1,5,4,1,4,9,4,1,4,4]))