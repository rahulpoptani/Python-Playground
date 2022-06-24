from Node import Node

n1 = Node(3)
n2 = Node(11)
n3 = Node(4)
n4 = Node(4)
n5 = Node(2)
n6 = Node(1)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

def sumTree(root: Node):
    if root == None: return 0
    return root.data + sumTree(root.left) + sumTree(root.right)

print(sumTree(n1))

def minValue(root: Node):
    stack = [root]
    minvalue = root.data
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
            minvalue = min(minvalue, current.right.data)
        if current.left:
            stack.append(current.left)
            minvalue = min(minvalue, current.left.data)
    return minvalue

print(f'MinValue in Tree is: {minValue(n1)}')

# Maximum Path Sum from Root to any Leaf
# incorrect
# def MaxPathSum(root: Node):
#     if root.left is None and root.right is None: return root.data
#     maxChildPathSum = max(MaxPathSum(root.left), MaxPathSum(root.right))
#     return root.data + maxChildPathSum


# print(MaxPathSum(n1))

