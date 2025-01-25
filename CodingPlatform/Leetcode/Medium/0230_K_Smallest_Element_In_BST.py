'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    n = 0
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right

# Unit Test
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.left.right = TreeNode(2)
print(kthSmallest(t, 1))

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.left.left.left = TreeNode(1)
print(kthSmallest(t, 3))

t = TreeNode(1)
t.right = TreeNode(2)
print(kthSmallest(t, 3))
