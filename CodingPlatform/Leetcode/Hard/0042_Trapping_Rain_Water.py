'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''

from typing import List

# Two pointer approach
def trap(height: List[int]) -> int:
    
    if not height: return 0

    l, r = 0, len(height)-1
    leftMax, rightMax = height[l], height[r]
    result = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            result += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            result += rightMax - height[r]
    
    return result

print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap(height = [4,2,0,3,2,5]))