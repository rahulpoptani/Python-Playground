import sys,os
sys.path.append(os.path.abspath(os.curdir))
from Node import Node
from TreeUtils import print_tree_visual

HASHES = 10

#       4
#     /   \
#    2     6
#   / \   / \
#  1   3 5   7


# Maximum Depth of Binary Tree
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

def maxDepth(root: Node):
    if not root: return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    return 1 + max(leftHeight, rightHeight)

print("#"*HASHES + " Max Height " + "#"*HASHES)
print_tree_visual(root)
print(f'Max Height: {maxDepth(root)}')

# Balanced Binary Tree (Difference in Height of Left Sub Tree and Right Sub Tree should be atmost 1)
#        1
#       /  \
#      3    2
#     /  \
#    5    4
#  /  \
# 7    8

# ImBalanced Tree
IBroot = Node(1)
IBroot.right = Node(2)
IBroot.left = Node(3)
IBroot.left.right = Node(4)
IBroot.left.left = Node(5)
IBroot.left.left.left = Node(7)
IBroot.left.left.right = Node(6)

def isBalancedBT(root):
    def checkHeight(node):
        if not node: 
            return 0
        
        leftHeight = checkHeight(node.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = checkHeight(node.right)
        if rightHeight == -1:
            return -1
        
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return 1 + max(leftHeight, rightHeight)  
    return checkHeight(root) != -1

print("#"*HASHES + " Balanced BT " + "#"*HASHES)
print_tree_visual(IBroot)
print(f'Balanced BT: {isBalancedBT(IBroot)}')

# Sum of all nodes
def sumTree(root: Node):
    if not root: return 0
    return root.value + sumTree(root.left) + sumTree(root.right)

print("#"*HASHES + " Sum of all Nodes " + "#"*HASHES)
print(f'Sum of all nodes: {sumTree(root)}')

# Minimum Value in Binary Tree
def minValue(root: Node):
    stack = [root]
    minvalue = root.value
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
            minvalue = min(minvalue, current.right.value)
        if current.left:
            stack.append(current.left)
            minvalue = min(minvalue, current.left.value)
    return minvalue

print("#"*HASHES + " Minimum value in BT " + "#"*HASHES)
print(f'MinValue in Tree: {minValue(root)}')

# Diameter of Binary Tree

#    1
#  /   \
# 2     3
#      /  \
#     4    6
#    /      \ 
#   5        7
#  /          \
# 9            8

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

print("#"*HASHES + " Diameter in BT " + "#"*HASHES)
print_tree_visual(root1)
print(f'MaxHeight: {diameter(root1,temp)} with diameter: {temp[0]}')

# Max Path Sum - Hint: Ignore negative path sum
temp = []
temp.append(0)
def maxPathSum(root, temp):
    if not root: return 0
    leftSum = max(0, maxPathSum(root.left, temp))
    rightSum = max(0, maxPathSum(root.right, temp))
    temp[0] = max(temp[0], leftSum + rightSum + root.value)
    return max(leftSum, rightSum) + root.value

print("#"*HASHES + " Max Path Sum " + "#"*HASHES)
print_tree_visual(root)
maxPathSum(root,temp)
print(f'MaxPathSum: {temp[0]}')

# Two Identical Binary Tree
def identicalBT(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        return (root1.value == root2.value
                and identicalBT(root1.left, root2.left)
                and identicalBT(root1.right, root2.right))
    return False

print("#"*HASHES + " Identical Tree " + "#"*HASHES)
print(f'Identical Tree: {identicalBT(root, root)}')
print(f'Identical Tree: {identicalBT(root, root1)}')

# Invert Binary Tree
def invertTree(root):
    if not root: return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

print("#"*HASHES + " Invert Binary Tree " + "#"*HASHES)
invertTree(root)
print('Inverted Tree')
print_tree_visual(root)

# Check Tree is Symmetrical
def are_symmetric(root1: Node, root2: Node):
    if root1 is None and root2 is None: 
        return True
    elif ((root1 is None) != (root2 is None)) or root1.value != root2.value: 
        return False
    else: 
        return are_symmetric(root1.left,root2.right) and are_symmetric(root1.right,root2.left)

def is_symettric(root):
    if root is None: return True
    return are_symmetric(root.left, root.right)

print(f'Is Symmetrical: {is_symettric(root)}')
sym = Node(4)
sym.left = Node(5)
sym.right = Node(5)
print(f'Is Symmetrical: {is_symettric(sym)}')

# Check if Tree is Subtree of another Tree
def isSubtree(root, sub):
    if not root: return False
    if are_symmetric(root, sub): return True
    return isSubtree(root.left, sub) or isSubtree(root.right, sub)

sub = Node(2)
sub.left = Node(1)
sub.right = Node(3)
print(f'Is Subtree: {isSubtree(root, sub)}')

