'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

from typing import List

def maxSubArray(nums: List[int]) -> int:
    maxSum = nums[0]
    currSum = 0
    
    for x in nums:
        if currSum < 0:
            currSum = 0
        currSum += x
        maxSum = max(maxSum, currSum)
    return maxSum
    


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))

# Algorithm Used: Kadane's Algorithm - Dynamic Programming Approach
# Time Complexity: O(n)
# Memory Complexity: O(1)

