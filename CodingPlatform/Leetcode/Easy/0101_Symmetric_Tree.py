'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''

from Common.Tags import BINARY_TREE, RECURSION
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    if root is None: return True

    def isMirror(left: TreeNode, right: TreeNode):
        # both nodes are empty
        if not left and not right:
            return True
        
        # one is empty
        if not left or not right:
            return False
        
        # values differ
        if left.val != right.val:
            return False
        
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return isMirror(root.left, root.right)
