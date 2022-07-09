'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:

    res = []
    nums.sort()

    length = len(nums)

    for i in range(length-2): # -2 because taking left and right pointers along with index

        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = length - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
        
    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))