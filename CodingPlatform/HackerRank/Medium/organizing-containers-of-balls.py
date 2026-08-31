'''
David has several containers, each with a number of balls in it.

David wants to perform some number of swap operations such that:
    Each container contains only balls of the same type.
    No two balls of the same type are located in different containers.
'''
from Common.Tags import ARRAY, MATRIX, GREEDY

def organizingContainers(container):
    n = len(container)

    container_sizes = [0] * n
    ball_type_counts = [0] * n

    for i in range(n):
        for j in range(n):
            balls = container[i][j]

            container_sizes[i] += balls
            ball_type_counts[j] += balls

    return (
        "Possible"
        if sorted(container_sizes) == sorted(ball_type_counts)
        else "Impossible"
    )

print(organizingContainers([[1, 1], [1, 1]]))  # Possible
print(organizingContainers([[1, 4], [2, 3]]))  # Impossible