'''
Given a binary tree, determine if it is height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''

from Common.Tags import RECURSION, BINARY_TREE
from DataStructures.Tree.TreeUtils import print_tree_visual
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def checkHeight(node):
        if not node: return 0
        leftHeight = checkHeight(node.left)
        if leftHeight == -1: return -1
        rightHeight = checkHeight(node.right)
        if rightHeight == -1: return -1
        if abs(leftHeight - rightHeight) > 1: return -1
        return 1 + max(leftHeight, rightHeight)
    return checkHeight(root) != -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(isBalanced(root))
print_tree_visual(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(3)
root.right.right.right.right = TreeNode(3)
root.right.right.right.right.right = TreeNode(3)
root.right.right.right.right.right.right = TreeNode(4)

print(isBalanced(root))
print_tree_visual(root)

root = None
print(isBalanced(root))
