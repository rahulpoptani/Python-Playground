from Node import Node
import sys
    
def isBST(node, min, max):
    if node is None: return True
    if node.data < min or node.data > max:
        return False
    return isBST(node.left, min, node.data-1) and isBST(node.right, node.data+1, max)


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
