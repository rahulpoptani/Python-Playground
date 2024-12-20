'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

'''

import os, sys
from typing import Optional
sys.path.append(os.path.abspath(os.curdir))
from DataStructures.Tree.TreeUtils import print_tree_visual

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root: return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invertTree(root.left)
    invertTree(root.right)
    return root

t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(7)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right.left = TreeNode(6)
t.right.right = TreeNode(9)

print_tree_visual(t)
invertTree(t)
print_tree_visual(t)
