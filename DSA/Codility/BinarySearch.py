def binary_search(arr, x):
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

arr = [1,2,3,4,5,6,7,8,9]

result = binary_search(arr, 8)

if result != -1:
    print('Found')
else:
    print('Not Found')


