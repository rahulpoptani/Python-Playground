'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

from Common.Tags import SLIDING_WINDOW

def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    best = float('inf')
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float('inf') else best

# Example usage:
print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
print(minSubArrayLen(4, [1,4,4]))        # Output: 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # Output: 0