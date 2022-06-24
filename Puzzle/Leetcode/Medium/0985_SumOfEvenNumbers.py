'''
You are given an integer array nums and an array queries where queries[i] = [val[i], index[i]]

Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Input: nums = [1], queries = [[4,0]]
Output: [0]
'''
from typing import List

def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    res = []
    for x,y in queries:
        nums[y] = nums[y] + x
        res.append( sum([z for z in nums if z % 2 == 0]) )
    return res


print(sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))

print(sumEvenAfterQueries([1], [[4,0]]))
        