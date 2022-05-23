# Given a sorted and rotated array, find if there is a pair with a given sum

# Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
# Output: true
# There is a pair (6, 10) with sum 16

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
# Output: true
# There is a pair (26, 9) with sum 35

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
# Output: false
# There is no pair with sum 45

def pairInSortedArray(arr, x):
    n = len(arr)
    # Find Pivot Point
    for i in range(n):
        if arr[i] > arr[i+1]:
            break
    left = i
    right = (i+1) % n
    print('Left: {} ({}) | Right: {} ({})'.format(left, arr[left], right, arr[right]))

    # Keep moving left and right direction based on current left+right elements sum
    while left != right:
        if arr[left] + arr[right] == x:
            print('Found at Left: {} ({}) | Right: {} ({})'.format(left, arr[left], right, arr[right]))
            return True
        # if the current pair sum is less, move to higher sum - increase right
        if arr[left] + arr[right] < x:
            right = (right + 1) % n
            print('New Right: {} ({})'.format(right, arr[right]))
        # else decrease left if current sum is less
        else:
            left = (left - 1 + n) % n
            print('New Left: {} ({})'.format(left, arr[left]))
    return False


arr = [11, 15, 6, 8, 9, 10]

print(pairInSortedArray(arr, 18))
