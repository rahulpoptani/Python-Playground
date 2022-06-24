from Node import Node

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

'''
      a
     / \
    b   c
   / \   \
  d   e   f
'''

def dfs(root: Node):
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        res.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print(res)

def bfs(root: Node):
    res = []
    queue = [root]
    while queue:
        current = queue.pop()
        res.append(current.data)
        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)
    print(res)

dfs(a)
bfs(a)

