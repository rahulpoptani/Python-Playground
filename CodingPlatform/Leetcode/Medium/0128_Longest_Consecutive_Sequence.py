'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.

Example 3:
Input: nums = [1, 0, 1, 2]
Output: 3
Explanation: There is no consecutive sequence, so the length will be 0.
'''

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best

print(longestConsecutive(nums = [100,4,200,1,3,2]))
print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive(nums = [1, 0, 1, 2]))