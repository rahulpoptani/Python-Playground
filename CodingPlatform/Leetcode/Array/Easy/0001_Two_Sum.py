from Common.Tags import GRIND_75
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
from Common.Tags import ARRAY, SET
from typing import List

# Bruteforce
def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(n²) - Uses nested loops where for each element, we potentially iterate through all remaining elements
    Space Complexity: O(1) - Only uses a constant amount of extra space for variables (toSearch, x, y)
    """
    for x in range(len(nums)):
        toSearch = target - nums[x]
        for y in range(x+1, len(nums)):
            if nums[y] == toSearch:
                return [x, y]


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

# Time and Space Complexity, both are O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    visit = {}
    for x in range(len(nums)):
        toSearch = target - nums[x]
        if toSearch in visit.keys():
            return [x, visit[toSearch]]
        else:
            visit[nums[x]] = x

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
