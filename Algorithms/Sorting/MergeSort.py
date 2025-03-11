
'''
Merge Sort is a divide-and-conquer sorting algorithm that:
    Divides the array into smaller subarrays (until each subarray contains a single element).
    Merges the subarrays in a sorted manner (two sorted arrays are merged into one sorted array).
'''

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements if any
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [2,3,5,1,7,4,4,4,2,6,0]
print(arr)
print(mergeSort(arr))


'''
Time Complexity => O (n logn)
Explaination:
    The array is split into two parts → O(log n) splits.
    Merging the arrays takes O(n) time.
    So total time = O(n log n).

Space Complexity => O(n) => Extra space is required to merge arrays.

Why is Merge Sort Efficient?
    Always O(n log n) time complexity regardless of input.
    Stable sort → Elements with equal keys appear in the same order.
    Can handle large datasets efficiently.
    Preferred in external sorting (sorting large files)

Why is Merge Sort Sometimes Inefficient?
    Requires extra space of O(n) for merging.
    Slower for small datasets compared to Quick Sort.
'''