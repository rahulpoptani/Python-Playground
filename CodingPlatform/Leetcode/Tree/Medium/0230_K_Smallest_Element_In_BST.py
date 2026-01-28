'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

from typing import Optional
from DataStructures.Tree.TreeUtils import print_tree_visual
from Common.Util import separator

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

# use inorder traversal which returns the value in sorted order and return the kth element
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    elements = []
    def inOrder(root):
        if root:
            inOrder(root.left)
            elements.append(root.value)
            inOrder(root.right)
    inOrder(root)
    return elements[k-1]

# Unit Test
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.left.right = TreeNode(2)
print_tree_visual(t)
print("kthSmallest", kthSmallest(t, 1))

separator("Tree 2")

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.left.left.left = TreeNode(1)
print_tree_visual(t)
print("kthSmallest", kthSmallest(t, 3))

