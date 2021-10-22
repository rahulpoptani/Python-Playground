# Cyclic Rotate the array from kth index


def solution(arr, k):
    result = [None] * len(arr)
    size = len(arr)
    for i in range(size):
        pos = (i + k) % size
        result[pos] = arr[i]
        # print(i, k, pos, result)
    return result

arr = [7,2,8,3,5]
print(arr)
print(solution(arr, 2))
