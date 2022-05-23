# A sorted array is rotated at some unknown point, find the minimum element in it. 

# Input: {5, 6, 1, 2, 3, 4}
# Output: 1

# Input: {1, 2, 3, 4}
# Output: 1

# Input: {2, 1}
# Output: 1

def findMin(arr, low, high):
    # if the array is not rotated at all
    if high < low:
        return arr[0]
    
    # if there is only one element left
    if high == low:
        return arr[low]
    
    mid = (low+high)//2

    # check if mid+1 is the minimum element?
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]
    
    # check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid-1]:
        return arr[mid]
    
    # decide we need to go left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)
    return findMin(arr, mid+1, high)

# The above approach in the worst case(If all the elements are the same) takes O(N).

# arr1 = [2, 3, 4, 5, 6, 7, 8, 9]
# n = len(arr1)
# print("The minimum element is " + str(findMin(arr1, 0, n-1)))

# Below is the code to handle duplicates elements in O(log n) time. 
def findMin2(arr, low, high):
    while (low < high):
        mid = low + (high - low)//2
        print('Current Middle Index: {} Element: {}'.format(mid, arr[mid]))

        if (arr[mid] == arr[high]):
            high -= 1
            print('New High: {} ({})'.format(high, arr[high]))
        elif (arr[mid] > arr[high]):
            low = mid + 1
            print('New Low: {} ({})'.format(low, arr[low]))
        else:
            high = mid
            print('New High From Mid: {} ({})'.format(high, arr[high]))
    return arr[high]



arr1 = [6, 7, 1, 2, 3, 4, 5]
n = len(arr1)
print("The minimum element is " + str(findMin2(arr1, 0, n-1)))

