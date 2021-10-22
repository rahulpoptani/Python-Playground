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

def pairInSortedRotated(arr, n, x):

    # Find the largest element which is also the pivot element
    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            print('Found pivot {} at {}'.format(arr[i], i))
            break
    
    left = i
    right = (i + 1) % n
    print('left (pivot): {} | right (pivot + 1): {}'.format(left, right))

    # Keep moving left and right direction based on current left+right elements sum
    while (left != right):
        if (arr[left] +  arr[right] == x):
            print('Found left: {} and right: {} with sum: {}'.format(arr[left], arr[right], x))
            return True
        # if the current pair sum is less, move to higher sum - increase right
        if (arr[left] + arr[right] < x):
            right = (right + 1) % n
            print('new right: {}'.format(right))
        else:
        # else decrease left if current sum is less
            left = (left - 1 + n) % n
            print('new left: {}'.format(left))
    
    return False





arr = [11, 15, 6, 8, 9, 10]

print(pairInSortedRotated(arr, len(arr), 16))
    