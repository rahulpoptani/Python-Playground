def solution(arr):
    num_open = 0
    for x in arr:
        if x == '(':
            num_open += 1
        else:
            num_open -= 1
        if num_open < 0:
            return 0
    if num_open == 0:
        return 1
    else:
        return 0

print(solution('(()(())())'))
print(solution('())'))