# O(n^2)
def maxSubArraySum(arr):
    best = 0
    for a in range(len(arr)):
        sum = 0
        for b in range(a, len(arr)):
            sum += arr[b]
            best = max(best, sum)
    return best

# O(n)
def maxSubArraySum(arr):
    sum, best = 0, 0
    for k in range(len(arr)):
        sum = max(arr[k], sum+arr[k])
        best = max(best, sum)
    return best

print(maxSubArraySum([-1,2,4,-3,5,2,-5,2]))