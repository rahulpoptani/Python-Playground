'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
'''
from Common.Tags import ARRAY, HASHMAP
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    
    return res

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(topKFrequent(nums = [1], k = 1))
print(topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))