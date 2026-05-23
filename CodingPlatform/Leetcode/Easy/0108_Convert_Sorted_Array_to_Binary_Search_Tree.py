'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

Example 2:
Input: nums = [1,3]
Output: [3,1]
'''

from Common.Tags import ARRAY, BINARY_TREE, DIVIDE_AND_CONQUER
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root

# Test cases
if __name__ == "__main__":
    # Example 1
    nums1 = [-10, -3, 0, 5, 9]
    tree1 = sortedArrayToBST(nums1)
    print(tree1.val)  # Output: 0

    # Example 2
    nums2 = [1, 3]
    tree2 = sortedArrayToBST(nums2)
    print(tree2.val)  # Output: 3