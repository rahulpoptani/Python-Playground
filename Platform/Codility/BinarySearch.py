
def binary_search(arr, ele):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low+high)//2
        if ele > arr[mid]:
            low = mid+1
        elif ele < arr[mid]:
            high = mid-1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(arr, 7)

if result != -1:
    print('Found at position: {}'.format(result))
else:
    print('Not Found')

