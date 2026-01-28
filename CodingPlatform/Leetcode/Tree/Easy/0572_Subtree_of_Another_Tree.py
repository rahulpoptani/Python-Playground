'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true 

Example 2: 
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''

from typing import Optional
from DataStructures.Tree.Node import Node as TreeNode
from DataStructures.Tree.TreeUtils import print_tree_visual

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isIdenticalTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        if root1 and root2 and root1.value == root2.value:
            return isIdenticalTree(root1.left, root2.left) and isIdenticalTree(root1.right, root2.right)
        return False
    
    if not subRoot: return True
    if not root: return False
    if isIdenticalTree(root, subRoot): return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
print_tree_visual(root)
print_tree_visual(subRoot)
print(isSubtree(root, subRoot))


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def serialize(node):
        def inOrder(node):
            if not node:
                array.append("#")
            else:
                array.append(str(node.value))
                inOrder(node.left)
                inOrder(node.right)
        array = []
        inOrder(node)
        return "/"+"/".join(array)
    s1 = serialize(root)
    s2 = serialize(subRoot)
    print(s1, s2)
    return s2 in s1

print(isSubtree(root, subRoot))
