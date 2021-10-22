# Fishes are swimming in opposite directions, bigger fish eats smaller fishes.
# How many fishes survived?
# Method takes two argument, one direction with 0 and 1 and another weight of fish

def solution(sizes, directions):
    stack = []
    escaped = 0
    for size, direction in zip(sizes, directions):
        if direction == 0:
            if stack:
                while stack and stack[-1] < size:
                    stack.pop()
                if not stack:
                    escaped += 1
            else:
                escaped += 1
        else:
            stack.append(size)

    return len(stack) + escaped

print(solution([4, 3, 2, 1, 5],[0, 1, 0, 0, 0]))

