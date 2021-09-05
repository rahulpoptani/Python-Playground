# A frog wants to get another side of the river. The array represent falling leaves at Kth time
# For example, you are given integer X = 5 and array A such that:
#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5

def solution(x, arr):
    position = {}
    for x in range(1, x+1):
        position[x] = True
    for x in range(len(arr)):
        try: 
            del position[arr[x]]
        except KeyError:
            None
        if len(position) == 0:
            return x
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))