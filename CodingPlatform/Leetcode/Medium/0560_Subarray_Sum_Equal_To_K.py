'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
i.e How many such subarrays are found whose sum is equal to k

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

Input: nums = [1,2,1,2,1], k = 3
Output: 4

'''
from Common.Tags import ARRAY, HASH, PREFIX_SUM
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    freq = {0: 1}  # base case: empty subarray has sum 0

    for num in nums:
        prefix_sum += num

        # Check if (prefix_sum - k) was seen before
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]

        # Record current prefix_sum
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))
print(subarraySum([1,2,1,2,1], 3))


