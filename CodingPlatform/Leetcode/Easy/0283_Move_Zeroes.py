'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
from Common.Tags import ARRAY, TWO_POINTER
from typing import List

def moveZeroes(nums: List[int]) -> None:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != pos:
                nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

# test cases
l1 = [1,2,3,4]
moveZeroes(l1)
print(l1)

l2 = [0,1,0,3,12]
moveZeroes(l2)
print(l2)

l3 = [0]
moveZeroes(l3)
print(l3)