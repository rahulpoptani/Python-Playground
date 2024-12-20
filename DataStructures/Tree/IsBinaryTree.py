from Node import Node
import sys
from TreeUtils import print_tree_visual
    
def isBST(node, min, max):
    if node is None: return True
    if node.value < min or node.value > max:
        return False
    return isBST(node.left, min, node.value-1) and isBST(node.right, node.value+1, max)


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

min = sys.float_info.min
max = sys.float_info.max

if (isBST(root,min,max)):
    print ("Is BST")
else:
    print ("Not a BST")

print_tree_visual(root)