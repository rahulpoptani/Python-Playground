'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

'''

from typing import List

def maxSubArray(nums: List[int]) -> int:
    total_sum = max_sum = nums[0]

    for x in nums[1:]:
        total_sum = max(total_sum+x, x)
        max_sum = max(max_sum, total_sum)
    
    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([-4,2,-5,1,2,3,6,-5,1]))
