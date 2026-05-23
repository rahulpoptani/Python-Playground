'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

from Common.Tags import ARRAY, BIT_MANIPULATION
from typing import List


def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

# Test cases
print(singleNumber([2, 2, 1]))  # Output: 1
print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(singleNumber([1]))  # Output: 1