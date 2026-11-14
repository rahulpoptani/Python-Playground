'''
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''

from typing import Optional
from Common.Tags import GRAPH, DFS, BFS

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None

    # Dictionary to keep track of cloned nodes
    cloned_nodes = {}

    def clone(node):
        if node in cloned_nodes:
            return cloned_nodes[node]

        # Create a new node with the same value
        new_node = Node(node.val)
        cloned_nodes[node] = new_node

        # Recursively clone the neighbors
        for neighbor in node.neighbors:
            new_node.neighbors.append(clone(neighbor))

        return new_node

    return clone(node)