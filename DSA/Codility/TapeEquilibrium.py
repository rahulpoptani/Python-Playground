# Find the minimum difference between left sub-array and right sub-array

def findMinDifference(arr):
    left_sum = arr[0]
    right_sum = sum(arr) - arr[0]
    diff = abs(left_sum - right_sum)

    for i in range(1, len(arr)):
        left_sum += arr[i]
        right_sum -= arr[i]
        curr_diff = abs(left_sum - right_sum)
        diff = min(diff, curr_diff)
    return diff

print(findMinDifference([3,1,2,4,3]))

