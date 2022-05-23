from BinaryTreeNode import BinarySearchTreeNode

def identicalTree(root1: BinarySearchTreeNode, root2: BinarySearchTreeNode):
    # if both tree have NULL root
    if not root1 and not root2:
        return True
    
    if root1 and root2:
        return (root1.data == root2.data
                and identicalTree(root1.left, root2.left)
                and identicalTree(root1.right, root2.right))
    
    return False


b1 = BinarySearchTreeNode(1)
b2 = BinarySearchTreeNode(1)

b1.add_child(2)
b1.add_child(3)

b2.add_child(2)
b2.add_child(3)


print(f'Tree 1 and Tree2 are identical?: {identicalTree(b1,b2)}')