def get_tree_height(node):
    if not node:
        return 0
    return 1 + max(get_tree_height(node.left), get_tree_height(node.right))

def fill_tree_matrix(matrix, node, row, col, gap):
    if not node:
        return
    matrix[row][col] = str(node.value)
    if node.left:
        fill_tree_matrix(matrix, node.left, row + 1, col - gap // 2, gap // 2)
    if node.right:
        fill_tree_matrix(matrix, node.right, row + 1, col + gap // 2, gap // 2)

def print_tree_visual(node):
    if not node:
        print("Tree is empty.")
        return
    height = get_tree_height(node)
    width = (2 ** height) * 2 - 1  # Full width of the tree matrix
    matrix = [[" " for _ in range(width)] for _ in range(height)]
    fill_tree_matrix(matrix, node, 0, width // 2, width // 2)
    for row in matrix:
        print("".join(row))