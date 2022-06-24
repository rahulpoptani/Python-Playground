graph = {
    'f': ['g','i'],
    'g': ['h'],
    'h': [],
    'i': ['g','k'],
    'j': ['i'],
    'k': []
}

def has_path(graph, source, destination):
    stack = [source]
    while stack:
        current = stack.pop()
        if current == destination: return True
        for x in graph[current][::-1]:
            stack.append(x)
    return False

print(has_path(graph, 'f', 'k'))
print(has_path(graph, 'j', 'f'))

