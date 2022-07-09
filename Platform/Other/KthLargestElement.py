'''
Given an array of integer arr and integer k, find the kth largest element.
arr = [4,2,9,7,5,6,7,1,3]
k = 4
Output: 6
Explanation:
1st largest: 9
2nd largest: 7
3rd largest: 7
4th largest: 6
'''

def kthLargestElement(arr, x):
    return sorted(arr)[len(arr)-x]

arr = [4,2,9,7,5,6,7,1,3]
print(kthLargestElement(arr,4))

# Using Heap - Default Python Implementation is MinHeap and not MaXHeap. Have to tweak for our login by adding negative sign
import heapq
def kth_largest(arr, k):
    arr = [-x for x in arr]         # O(n)
    heapq.heapify(arr)              # O(n)
    for i in range(k-1):            # (k-1)
        heapq.heappop(arr)          # logn
    return -heapq.heappop(arr)      # logn

print(kth_largest(arr, 4))

# Time: 2n + (k-1) * logn + logn => 2n + klogn => O(n + klogn)