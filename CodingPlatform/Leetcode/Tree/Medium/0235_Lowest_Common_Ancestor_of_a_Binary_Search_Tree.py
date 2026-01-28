'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
'''

import os, sys
sys.path.append(os.path.abspath(os.curdir))
from DataStructures.Tree.TreeUtils import print_tree_visual
from Common.Tags import GRIND_75

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr = root
    while curr:
        if p.value > curr.value and q.value > curr.value:
            curr = curr.right
        elif p.value < curr.value and q.value < curr.value:
            curr = curr.left
        else:
            return curr

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

print('LCA of 2 and 8 =>', lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).value)
print('LCA of 3 and 4 =>', lowestCommonAncestor(root, TreeNode(3), TreeNode(4)).value)
print('LCA of 5 and 0 =>', lowestCommonAncestor(root, TreeNode(5), TreeNode(0)).value)

print_tree_visual(root)

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or not p or not q: return None
    if (max(p.value, q.value) < root.value):
        return lowestCommonAncestor(root.left, p, q)
    elif (min(p.value, q.value) > root.value):
        return lowestCommonAncestor(root.right, p, q)
    return root

print('LCA of 2 and 8 =>', lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).value)
print('LCA of 3 and 4 =>', lowestCommonAncestor(root, TreeNode(3), TreeNode(4)).value)
print('LCA of 5 and 0 =>', lowestCommonAncestor(root, TreeNode(5), TreeNode(0)).value)
