'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
such that i < j < k and nums[i] < nums[k] < nums[j]
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

def find132Pattern(nums):
    stack = []
    curMin = nums[0]

    for n in nums[1:]:
        while stack and n >= stack[-1][1]:
            stack.pop()
        if stack and n > stack[-1][0]:
            return True
        curMin = min(curMin, n)
        stack.append([curMin, n])
    return False

print(find132Pattern([1,2,3,4]))
print(find132Pattern([3,1,4,2]))
print(find132Pattern([-1,3,2,0]))   