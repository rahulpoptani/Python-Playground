
from TreeUtils import print_tree_visual

class BinarySearchTreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.value: return
        if data < self.value:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.value)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.value)
        return elements
    
    def search(self, val):
        if self.value == val:
            return True
        if val < self.value:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.value:
            if self.right:
                return self.right.search(val)
            else:
                return False

def buildBinarySearchTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = buildBinarySearchTree(numbers)
    print("In", numbers_tree.in_order_traversal())
    print("Pre", numbers_tree.pre_order_traversal())
    print("Post", numbers_tree.post_order_traversal())
    print_tree_visual(numbers_tree)
