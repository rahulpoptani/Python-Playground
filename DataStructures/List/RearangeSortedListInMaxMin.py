# Rearrange sorted list in Max/Min Form
# 0th Index = Maximum Value
# 1st Index = Minimum Value
# 2nd Index = 2nd Maximum Value
# 3rd Index = 2nd Minimum Value, and so on.

import math
def max_min(lst):
    maxIndex = 0
    minIndex = 1
    end = len(lst)-1
    start = 0
    res = []
    while (start < end):
        res.insert(maxIndex, lst[end])
        res.insert(minIndex, lst[start])
        start += 1
        end -= 1
        maxIndex += 2
        minIndex += 2
    if len(lst) % 2 == 1:
        res.append(lst[ math.floor(len(lst)/2) ])
    return res


print(max_min([1,2,3,4,5,6,7,8,9]))
print(max_min([1,1,1,1,1]))


def max_min2(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):
        result.append(lst[-(i+1)])
        result.append(lst[i])
    if len(lst) % 2 == 1:
        # if middle value then append
        result.append(lst[len(lst)//2])
    return result


print(max_min2([1,2,3,4,5,6,7,8,9]))
print(max_min2([1,1,1,1,1]))

# Time Complexity: O(n) as the list is iterated once