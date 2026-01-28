'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

from typing import Optional
from DataStructures.Tree.Node import Node
from DataStructures.Tree.TreeUtils import print_tree_visual
from Common.Util import separator

def isValidBST(root: Optional[Node]) -> bool:
   def validate(node: Node, low: int, high: int) -> bool:
      if not node: return True
      if not (low < node.value < high): return False
      return validate(node.left, low, node.value) and validate(node.right, node.value, high)
   return validate(root, float("-inf"), float("inf"))

root = Node(2)
root.left = Node(1)
root.right = Node(3)
print_tree_visual(root)
print(isValidBST(root))

separator("Test")

root = Node(5)
root.left = Node(1)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)
print_tree_visual(root)
print(isValidBST(root))

root = Node(0)
print_tree_visual(root)
print(isValidBST(root))
