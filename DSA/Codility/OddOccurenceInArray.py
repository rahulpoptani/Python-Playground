# Array with N odd number of elements, each element can be paired with itself, only 1 cannot pair. Identify the odd


def solution(arr):
    found = {}
    for x in arr:
        try:
            del found[x]
        except:
            found[x] = 1
    if len(found) == 1:
        return found.keys()

print(solution([9, 3, 9, 3, 9, 7, 9]))