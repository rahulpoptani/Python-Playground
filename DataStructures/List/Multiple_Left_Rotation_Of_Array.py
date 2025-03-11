from Common.Tags import ARRAY, ARRAY_ROTATION
# Given an array of size n and multiple values around which we need to left rotate the array.
# How to quickly find multiple left rotations?

# Step 1: Copy the entire array two times in temp[0..2n-1] array. 
# Step 2: Starting position of array after k rotations in temp[] will be k % n. We do k 
# Step 3: Print temp[] array from k % n to k % n + n.

# O(n) time and O(1) extra space

# fill temp with 2 copies of array
def preprocess(arr, n):
    temp = [None] * (2 * n)
    for x in range(n):
        temp[x] = temp[x + n] = arr[x]
    return temp

# function to left rotate the array k times
def leftRotate(n, k, temp):
    # starting position of array after k rotations
    start = k % n

    # print array after k rotations
    for x in range(start, start + n):
        print(temp[x], end=" ")
    print()


arr = [1, 3, 5, 7, 9]
n = len(arr)
temp = preprocess(arr, n)

k = 2
leftRotate(n, k, temp)

k = 3
leftRotate(n, k, temp)

k = 4
leftRotate(n, k, temp)

k = 5
leftRotate(n, k, temp)

k = 6
leftRotate(n, k, temp)

# Another approach which does not takes extra space like above
print('----------')
def leftRotate2(arr, n, k):
    for x in range(k, k+n):
        print(arr[x % n], end=' ')
    print()


k = 2
leftRotate2(arr, n, k)

k = 3
leftRotate2(arr, n, k)

k = 4
leftRotate2(arr, n, k)

k = 5
leftRotate2(arr, n, k)

k = 6
leftRotate2(arr, n, k)