'''
We need to check the Horizontal Distances from the root for all nodes. 
If two nodes have the same Horizontal Distance (HD), then they are on the same vertical line.
           1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 

The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

HD for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance 
and a left edge is considered as -1 horizontal distance. 
For example, in the above tree, HD for Node 4 is at -2, 
HD for Node 2 is -1, 
HD for 5 and 6 is 0 and 
HD for node 7 is +2. 

We can do preorder traversal of the given Binary Tree. While traversing the tree, we can recursively calculate HD
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
def getVerticalOrder(root,hd,m):
    if root is None:
        return
    try:
        m[hd].append(root.data)
    except:
        m[hd] = [root.data]
    # Store nodes in left subtree
    getVerticalOrder(root.left,hd-1,m)
    # Store nodes in right subtree
    getVerticalOrder(root.right,hd+1,m)


def printVerticalOrder(root):
    # Create Map and store vertical order
    m = dict()
    hd = 0 # Horizontal Distance
    getVerticalOrder(root,hd,m)
    # Traverse the map and print the nodes
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i,end=' ')
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print ("Vertical order traversal is")
printVerticalOrder(root)