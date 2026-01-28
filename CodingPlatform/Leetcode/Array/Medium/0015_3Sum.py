'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''
from Common.Tags import ARRAY, TWO_POINTER
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

print(threeSum(nums = [-1,0,1,2,-1,-4]))
print(threeSum(nums = [0,1,1]))
print(threeSum(nums = [0,0,0]))

'''
Time Complexity: O(n^2).
    Sorting the array takes O(n log n), where n is the length of the input array.
    The main loop iterates through the array, and for each element, a two-pointer approach is used to find pairs that sum to the target. The two-pointer approach runs in O(n) for each iteration.
    In the worst case, the main loop runs O(n) times, so the total time complexity is O(n^2).

Space Complexity: O(1)
    The solution uses O(1) additional space for variables and pointers.
    The result list res is not considered in the space complexity since it depends on the output size, which is determined by the input.
    Thus, the overall space complexity is O(1) (excluding the output).
'''