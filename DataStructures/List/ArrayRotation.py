
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()

def reverseArray(arr, start, end):
    while(start < end):
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1

# Left Rotate by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is greater than array length
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)


arr = [1,2,3,4,5]

printArray(arr)

leftRotate(arr, 2)

printArray(arr)

# Time Complexity: O(n)
