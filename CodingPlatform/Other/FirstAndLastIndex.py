'''
Find first and last index in a sorted array
Given a sorted array of integer "arr" and integer "target"
Find the index of first and last position of "target" in "arr". If not found then return [-1,-1]

Input:
arr = [2,4,5,5,5,5,5,7,9,9]
target = 5
output: [2,6]
'''

def find_first_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target: return [-1,-1]
    start = findstart(arr,target)
    end = findend(arr,target)
    return [start,end]
    
def findstart(arr, target):
    if arr[0] == target:
        return 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target and arr[mid-1] < arr[mid]:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def findend(arr, target):
    if arr[-1] == target:
        return len(arr)-1
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target and arr[mid+1] > arr[mid]:
            return mid
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1  

print(find_first_last([2,4,5,5,5,5,5,7,9,9], 5))
print(find_first_last([5,5,5,5,5], 5))

# Time Complexity: 2 * O(logn) = O(logn)
# Space: O(1)