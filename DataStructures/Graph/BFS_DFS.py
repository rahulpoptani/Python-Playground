graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def dfs(graph, source):
    res = []
    stack = [source]
    while stack:
        current = stack.pop()
        res.append(current)
        for x in graph[current][::-1]:
            stack.append(x)
    return res

def bfs(graph, source):
    res = []
    queue = [source]
    while queue:
        current = queue.pop()
        res.append(current)
        for x in graph[current]:
            queue.insert(0,x)
    return res

print(dfs(graph, 'a'))
print(bfs(graph, 'a'))

