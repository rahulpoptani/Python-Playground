
def binarySearchIterative(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            return mid
    return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
print(f'BinarySearch Iterative: {binarySearchIterative(arr,x)}')

def binarySearchRecursive(arr,low,high,x):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(arr,low,mid-1,x)
        else:
            return binarySearchRecursive(arr,mid+1,high,x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
low = 0
high = len(arr)-1
print(f'BinarySearch Recursive: {binarySearchRecursive(arr,low,high,x)}')
