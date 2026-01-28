'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
i.e How many such subarrays are found whose sum is equal to k

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

Input: nums = [1,2,1,2,1], k = 3
Output: 4

Input: nums = [3,4,7,2,-3,1,4,2], k = 7
Output: 4
'''
from Common.Tags import ARRAY, HASH
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    sumdict = {0:1}
    count = 0
    sum = 0

    for num in nums:
        sum += num
        if sum - k in sumdict:
            count += sumdict[sum - k]
        
        if sum in sumdict:
            sumdict[sum] += 1
        else:
            sumdict[sum] = 1
        
        print(f'Num: {num:2d} | Sum: {sum:2d} | Sum-K: {sum-k:2d} | Count: {count:2d} | Sumdict: {sumdict}')
    
    return count


# print(subarraySum([1,1,1], 2))
# print(subarraySum([1,2,3], 3))
# print(subarraySum([1,2,1,2,1], 3))
print(subarraySum([3,4,7,2,-3,1,4,2,1], 7))


    