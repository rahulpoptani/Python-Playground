import sys,os
sys.path.append(os.path.abspath(os.curdir))
from Node import Node
from collections import deque
from DataStructures.Stack.Stack import Stack

'''
      4
    /   \
   2     6
  / \   / \
 1   3 5   7
'''

# Maximum Depth of Binary Tree
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

def maxDepth(root):
    if not root: return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    return 1 + max(leftHeight, rightHeight)

print(f'Max Height: {maxDepth(root)}')

# Balanced Binary Tree (Difference in Height of Left Sub Tree and Right Sub Tree should be atmost 1)
'''
       1
      /  \
     3    2
    /  \
   5    4
 /  \
7    8
'''
# ImBalanced Tree
IBroot = Node(1)
IBroot.right = Node(2)
IBroot.left = Node(3)
IBroot.left.right = Node(4)
IBroot.left.left = Node(5)
IBroot.left.left.left = Node(7)
IBroot.left.left.right = Node(6)

def isBalancedBT(root):
    if not root: return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    if leftHeight == -1 or rightHeight == -1: return -1
    if (abs(leftHeight - rightHeight) > 1): return -1
    return 1 + max(leftHeight, rightHeight)

print(f'Balanced BT: {isBalancedBT(IBroot)}')

# Sum of all nodes
def sumTree(root: Node):
    if root == None: return 0
    return root.value + sumTree(root.left) + sumTree(root.right)

print(f'Sum of all nodes: {sumTree(root)}')

# Minimum Value in Binary Tree
def minValue(root: Node):
    stack = [root]
    minvalue = root.value
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
            minvalue = min(minvalue, current.right.data)
        if current.left:
            stack.append(current.left)
            minvalue = min(minvalue, current.left.data)
    return minvalue

print(f'MinValue in Tree: {minValue(root)}')

# Diameter of Binary Tree
'''
   1
 /   \
2     3
     /  \
    4    6
   /      \ 
  5        7
 /          \
9            8
'''
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.right.left = Node(4)
root1.right.left.left = Node(5)
root1.right.left.left.left = Node(9)
root1.right.right = Node(6)
root1.right.right.right = Node(7)
root1.right.right.right.right = Node(8)

temp = []
temp.append(0) # why sending as list and not a variable, because this way we are passing reference of an object, string object will be immutable and won't work in this case
def diameter(root, temp):
    if not root: return 0
    leftHeight = diameter(root.left, temp)
    rightHeight = diameter(root.right, temp)
    temp[0] = max(temp[0], leftHeight + rightHeight)
    return 1 + max(leftHeight, rightHeight)

print(f'MaxHeight: {diameter(root1,temp)} with diameter: {temp[0]}')

# Max Path Sum - Hint: Ignore negative path sum
temp = []
temp.append(0)
def maxPathSum(root, temp):
    if not root: return 0
    leftSum = max(0, maxPathSum(root.left, temp))
    rightSum = max(0, maxPathSum(root.right, temp))
    temp[0] = max(temp[0], leftSum + rightSum + root.data)
    return max(leftSum, rightSum) + root.data

maxPathSum(root,temp)
print(f'MaxPathSum: {temp[0]}')

# Two Identical Binary Tree
def identicalBT(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        return (root1.data == root2.data
                and identicalBT(root1.left, root2.left)
                and identicalBT(root1.right, root2.right))
    return False

print(f'Identical Tree: {identicalBT(root, root)}')
print(f'Identical Tree: {identicalBT(root, root1)}')