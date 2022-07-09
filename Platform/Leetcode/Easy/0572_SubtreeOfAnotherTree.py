'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root 
with the same structure and node values of subRoot and false otherwise.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Images:
https://leetcode.com/problems/subtree-of-another-tree/
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def issame(s, t):
        if s is None and t is None:
            return  True
        if s is None or t is None:
            return False
        return s.val == t.val and issame(s.left, t.left) and issame(s.right, t.right)
    
    if root is None and subRoot is None:
        return True
    if subRoot is None:
        return True
    if root is None and subRoot is not None:
        return False
    return issame(root, subRoot) or issame(root.left, subRoot) or issame(root.right, subRoot)