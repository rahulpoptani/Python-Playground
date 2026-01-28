def get_tree_height(node):
    if not node:
        return 0
    return 1 + max(get_tree_height(node.left), get_tree_height(node.right))

def calculate_positions(node, level=0, position=0, positions=None):
    """Calculate the position of each node using in-order traversal."""
    if positions is None:
        positions = {}
    
    if not node:
        return position, positions
    
    # Process left subtree
    position, positions = calculate_positions(node.left, level + 1, position, positions)
    
    # Current node gets the next position
    positions[id(node)] = (level, position, len(str(node.value)))
    position += 1
    
    # Process right subtree
    position, positions = calculate_positions(node.right, level + 1, position, positions)
    
    return position, positions

def fill_tree_matrix(matrix, node, positions, col_offset):
    """Fill the matrix with node values at calculated positions."""
    if not node:
        return
    
    level, col, width = positions[id(node)]
    value_str = str(node.value)
    
    # Place the value in the matrix
    actual_col = col * 2 + col_offset  # Add spacing between columns
    for i, char in enumerate(value_str):
        if actual_col + i < len(matrix[level]):
            matrix[level][actual_col + i] = char
    
    # Process children
    fill_tree_matrix(matrix, node.left, positions, col_offset)
    fill_tree_matrix(matrix, node.right, positions, col_offset)

def print_tree_visual(node):
    if not node:
        print("Tree is empty.")
        return
    
    # First pass: calculate positions for all nodes
    max_position, positions = calculate_positions(node)
    
    # Determine the height and width needed
    height = max(pos[0] for pos in positions.values()) + 1
    width = max_position * 2  # Add spacing between columns
    
    # Create matrix
    matrix = [[" " for _ in range(width)] for _ in range(height)]
    
    # Second pass: fill the matrix
    fill_tree_matrix(matrix, node, positions, 0)
    
    # Print the matrix
    for row in matrix:
        print("".join(row))