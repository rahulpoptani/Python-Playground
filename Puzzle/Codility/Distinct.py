# Given an array return number of distinct values

# Approach 1
def solution(arr):
    distinct = {}
    for x in arr:
        distinct[x] = True
        print(distinct)
    return len(distinct)

arr = [2,1,1,3,4,4,4,3]
print(solution(arr))

# Approach 2
print(len(set(arr)))

