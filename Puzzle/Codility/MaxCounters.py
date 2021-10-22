# Create method which takes size of counter and array. For every element from array it will maintain the frequency,
# once element with greater than counter encounter, it will reset all frequencies to max available counter
# Example: size of counter = 5 and array = [3,4,4,6,1,4,4]
# Assum the minimum value in source arrray will be 1
# 3 => [0,0,1,0,0]
# 4 => [0,0,1,1,0]
# 4 => [0,0,1,2,0]
# 6 => [2,2,2,2,2] Since result array contains 2 as the max_counter, all element will be converted to max_counter = 2
# 1 => [3,2,2,2,2]
# 4 => [3,2,2,3,2]
# 4 => [3,2,2,4,2]


def maxCounter(n,arr):
    result = [0] * n
    for x in arr:
        if x > n:
            setalltomax(result)
        else:
            result[x-1] += 1
    return result

def setalltomax(arr):
    maxvalue = max(arr)
    for i in range(len(arr)):
        arr[i] = maxvalue




print(maxCounter(5, [3,4,4,6,1,4,4]))

