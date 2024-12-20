
def printArray(arr):
    for x in arr:
        print(x, end = " ")
    print()

def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Time Complexity: O(n)
# Left Rotate by d
def rightRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    d = d % n  # if the rotating factor is greater than array length
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

# Right Rotate by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    d = d % n  # if the rotating factor is greater than array length
    reverseArray(arr, 0, n-1)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)


arr = [1,2,3,4,5]
printArray(arr)

rightRotate(arr, 2)
printArray(arr)

arr = [1,2,3,4,5]
rightRotate(arr, 7)
printArray(arr)

arr = [1,2,3,4,5]
leftRotate(arr, 2)
printArray(arr)
