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
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            break
    left = i
    right = (i+1) #% n
    print(f'Start left: {left} {arr[left]} | Start right: {right} {arr[right]} | Sum: {arr[left] + arr[right]}')

    # Keep moving left and right direction based on current left+right elements sum
    while left != right:
        if arr[left] + arr[right] == x:
            print(f'Found left: {left} {arr[left]} | right: {right} {arr[right]}')
            return True
        # if the current pair sum is less, move to higher sum - increase right
        if arr[left] + arr[right] < x:
            right = (right + 1) % n
            print(f'left: {left} {arr[left]} | New right: {right} {arr[right]} | Sum: {arr[left] + arr[right]}')
        # else decrease left if current sum is less
        else:
            left = (left - 1 + n) % n
            print(f'New left: {left} {arr[left]} | right: {right} {arr[right]} | Sum: {arr[left] + arr[right]}')
    return False


arr = [11, 15, 6, 8, 9, 10]
print(pairInSortedArray(arr, 18))

print()
arr = [6, 8, 9, 10]
print(pairInSortedArray(arr, 18))

print()
arr = [6, 8, 9, 10]
print(pairInSortedArray(arr, 22))

print()
arr = [6, 8, 9, 10, 1]
print(pairInSortedArray(arr, 18))
