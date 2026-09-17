'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
'''

from DataStructures.Tree.TreeUtils import print_tree_visual
from Common.Tags import DESIGN, BINARY_TREE, DFS

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        result = []

        def dfs(node):
            if node is None:
                result.append('N')
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(result)

    def deserialize(self, data):
        values = iter(data.split(','))

        def dfs():
            value = next(values)
            if value == 'N':
                return None

            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Example Usage:
codec = Codec()
tree = codec.deserialize("1,2,N,N,3,4,N,N,5,N,N")
serialized_tree = codec.serialize(tree)
print_tree_visual(tree)
print("Serialized Tree:", serialized_tree)
