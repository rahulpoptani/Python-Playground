# Given an array return number of distinct values

def solution(arr):
    distinct = {}
    for x in arr:
        distinct[x] = True
    return len(distinct)

print(solution([2,1,1,3,4,4,4,3]))