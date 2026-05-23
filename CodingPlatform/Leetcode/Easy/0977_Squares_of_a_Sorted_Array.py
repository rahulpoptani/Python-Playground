'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

from Common.Tags import ARRAY, TWO_POINTER
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1

    pos = n - 1
    while left <= right:

        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result

# Test cases
print(sortedSquares([-4,-1,0,3,10]))  # Output: [0,1,9,16,100]
print(sortedSquares([-7,-3,2,3,11]))  # Output: [4,9,9,49,121]