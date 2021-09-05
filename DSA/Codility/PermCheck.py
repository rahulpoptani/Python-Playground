# A array containing sequence of numbers from 1 to N once and only once


def solution(arr):
    dict = {}
    for x in range(1, len(arr)+1):
        dict[x] = True
    for x in arr:
        try:
            del dict[x]
        except KeyError:
            return 0
    return 1

print(solution([2, 1, 4, 3]))
