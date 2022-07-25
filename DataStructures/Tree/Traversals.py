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
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

# In Order Traversal Left-Root-Right
elements = []
def inOrder(root):
    if root:
        inOrder(root.left)
        elements.append(root.data)
        inOrder(root.right)

inOrder(root)
print('InOrder ->', elements)

elements = []
def InOrderIterative(root):
    stack = []
    node = root
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if not stack: return
            node = stack.pop()
            elements.append(node.data)
            node = node.right

InOrderIterative(root)
print('InOrder Iterative ->', elements)

# Pre Order Traversal Root-Left-Right
elements = []
def preOrder(root):
    if root:
        elements.append(root.data)
        preOrder(root.left)
        preOrder(root.right)

preOrder(root)
print('PreOrder ->', elements)

# Post Order Traversal Left-Right-Root
elements = []
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        elements.append(root.data)

postOrder(root)
print('PostOrder ->', elements)

elements = []
def postOrderIterative2Stack(root):
    stack1 = [root]
    stack2 = []
    while stack1:
        current = stack1.pop()
        stack2.append(current.data)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    while stack2:
        elements.append(stack2.pop())

postOrderIterative2Stack(root)
print('PostOrder Iterative 2 Stacks ->', elements)

elements = []
def postOrderIterative1Stack(root):
    stack = Stack()
    current = root
    while current or stack:
        if current:
            stack.push(current)
            current = current.left
        else:
            temp = stack.peek().right
            if temp:
                current = temp
            else:
                temp = stack.pop()
                elements.append(temp.data)
                while stack and temp == stack.peek().right:
                    temp = stack.pop()
                    elements.append(temp.data)

postOrderIterative1Stack(root)
print('PostOrder Iterative 1 Stacks ->', elements)

# BFS / Level Order Traversal
elements = []
def bfs(root):
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        elements.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

bfs(root)
print('BFS/Level Order ->', elements)

# ZigZag Traversal
elements = []
def zigzag(root):
    if not root: return elements
    direction = False
    queue = deque()
    queue.append(root)
    while queue:
        size = len(queue)
        temp = [None] * size
        for x in range(size):
            current = queue.popleft()
            if direction:
                temp[x] = current.data
            else:
                temp[size - 1 - x] = current.data
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        direction = not direction
        elements.extend(temp)

zigzag(root)
print('ZigZag ->', elements)

# Mark Level
elements = []
def markLevel(root):
    queue = deque()
    level = 1
    queue.append([level, root])
    while queue:
        current = queue.popleft()
        elements.append([current[0], current[1].data])
        if current[1].left:
            queue.append([current[0]+1, current[1].left])
        if current[1].right:
            queue.append([current[0]+1, current[1].right])

markLevel(root)
print('Mark Level ->', elements)

# DFS / PreOrder Iterative
elements = []
def dfs(root):
    stack = [root]
    while stack:
        current = stack.pop()
        elements.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

dfs(root)
print('DFS ->', elements)

# Boundary Traversal
elements = []
def boundaryTraversal(root):
    # print leaves
    def printLeaves(root):
        if root:
            printLeaves(root.left)
            if not root.left and not root.right:
                elements.append(root.data)
            printLeaves(root.right)
    
    # print left boundary
    def printLeftBoundary(root):
        if root:
            if root.left:
                elements.append(root.data)
                printLeftBoundary(root.left)
            elif root.right:
                elements.append(root.data)
                printLeftBoundary(root.right)
    
    # print right boundary
    def printRightBoundary(root):
        if root:
            if root.right:
                printRightBoundary(root.right)
                elements.append(root.data)
            elif root.left:
                printRightBoundary(root.left)
                elements.append(root.data)
    
    if root:
        elements.append(root.data)
        printLeftBoundary(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printRightBoundary(root.right)

boundaryTraversal(root)
print('Boundary Traversal ->', elements)
