'''
A Tree is considered symmetrical when mirror image of left subree is equal to right subtree
'''

from Node import Node

def are_symmetric(root1: Node, root2: Node):
    if root1 is None and root2 is None: 
        return True
    elif ((root1 is None) != (root2 is None)) or root1.value != root2.value: 
        return False
    else: 
        are_symmetric(root1.left,root2.right) and are_symmetric(root1.right,root2.left)

def is_symettric(root):
    if root is None: return True
    return are_symmetric(root.left, root.right)


root = Node(4)
root.left = Node(5)
root.right = Node(5)

print(is_symettric(root))




