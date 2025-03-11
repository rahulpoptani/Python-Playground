'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

from typing import List

# def findKthLargest(nums: List[int], k: int) -> int:
#     nums.sort()
#     return nums[len(nums) - k]

# print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
# print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))

def findKthLargest(nums: List[int], k: int) -> int:
    # the index we are looking for, if the array was sorted
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l # Choose the rightmost element as the pivot
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p] # Swap elements to partition the array
                p += 1
        
        nums[p], nums[r] = nums[r], nums[p] # Place the pivot in its correct position

        # Recursively apply quickSelect to the appropriate partition
        if k < p:   return quickSelect(l, p - 1)  # Search in the left partition
        elif k > p: return quickSelect(p + 1, r)  # Search in the right partition
        else:       return nums[p]  # Found the kth largest element
    
    return quickSelect(0, len(nums) - 1)  # Start the quickSelect process

print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
