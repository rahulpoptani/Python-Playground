'''
N-Repeated Elements in size 2N Array
Input: nums = [1,2,3,3]
Output: 3
Input: nums = [2,1,2,5,3,2]
Output: 2
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
'''
from typing import List

def repeatedNTimes(nums: List[int]) -> int:
    visit = set()
    for x in nums:
        if x not in visit:
            visit.add(x)
        else:
            return x

print(repeatedNTimes([1,2,3,3]))
print(repeatedNTimes([2,1,2,5,3,2]))
print(repeatedNTimes([5,1,5,2,5,3,5,4]))