'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    prod, zero_cnt = 1, 0
    for num in nums:
        if num:
            prod *= num
        else:
            zero_cnt +=  1
    if zero_cnt > 1: return [0] * len(nums)

    res = [0] * len(nums)
    for i, c in enumerate(nums):
        if zero_cnt: res[i] = 0 if c else prod
        else: res[i] = prod // c
    return res

print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([1, 2, 0, 4]))
print(productExceptSelf([1, 2, 0, 0]))