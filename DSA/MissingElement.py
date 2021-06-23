# Find the minimal positive integer not occurring in the given sequence.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.

def solution(arr):
    missing = 1
    for x in sorted(arr):
        if x == missing:
            missing += 1
        if x > missing:
            break
    return missing

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))