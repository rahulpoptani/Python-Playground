# Find number of connected components
# Connected Component are graphs which are connect with nodes. Count of such individual graphs

graph = {
    1: [2],
    2: [1],
    3: [],
    4: [6],
    5: [6],
    6: [4,5,7,8],
    7: [6],
    8: [6],
}
# In the above graph we have 3 such individual graphs. 
# 1. [1,2]
# 2. [4,5,6,7]
# 3. [3]

print(graph)

# def connected_components(graph):
#     visited = set()
#     for x,y in graph:

