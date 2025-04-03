# Undirected Edges between two nodes
edges = [ ['i','j'], ['k','i'], ['m','k'],['k','l'],['o','n'] ]

# From the edges, we need to convert into an adjaceny list
graph = {}
for x,y in edges:
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x].append(y)
    if y not in graph:
        graph[y] = [x]
    else:
        graph[y].append(x)

print(graph)

def has_path(graph, source, destination):
    visited = set()
    stack = [source]
    while stack:
        current = stack.pop()
        visited.add(current)
        if current == destination: return True
        for x in graph[current][::-1]:
            if x not in visited:
                stack.append(x)
    return False

print(has_path(graph, 'i', 'l'))
print(has_path(graph, 'i', 'o'))

