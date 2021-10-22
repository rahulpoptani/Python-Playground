# Find the rotation count in rotated sorted array

# Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

# Input : arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation : Initial array must be {2, 3,
# 6, 12, 15, 18}. We get the given array after 
# rotating the initial array twice.

# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4

# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0

# Using Linear Search approach, we can notice that the number of rotations is equal to index+1 of minimum element
def countRotations1(arr):
    for x in range(len(arr)-1):
        if arr[x] > arr[x+1]:
            break
    return x+1

# O(n)
arr1 = [15, 18, 2, 3, 6, 12]
arr2 = [7, 9, 11, 12, 5]

print(countRotations1(arr1))
print(countRotations1(arr2))


# O(log n)
def countRotations2(arr):
    n = len(arr)
    start = 0
    end = n-1
    
    # find index of minimum element in array, the index will be number of rotations
    while (start <= end):
        mid = start + (end - start) // 2
        # calculate previous and next of mid
        prev = (mid - 1 + n) % n
        next = (mid + 1 + n) % n
        # checking if mid is minimum
        if (arr[mid] < arr[prev] and arr[mid] <= arr[next]): return mid
        # if not selecting the unsorted part of array
        elif (arr[mid] < arr[start]): end = mid - 1
        elif (arr[mid] > arr[end]): start = mid + 1
        else: return 0


print(countRotations2(arr1))
print(countRotations2(arr2))



