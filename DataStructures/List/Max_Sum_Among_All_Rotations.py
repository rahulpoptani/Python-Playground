# Maximum of i * arr[i] among all rotations of a given array

# The basic approach is to calculate the sum of new rotation from the previous rotations

# next_val = curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1)
# next_val = sum of value of i * arr[i] for all elements after one rotation
# curr_val = current sum of i * arr[i] for all element 
# cum_sum = Sum of all array elements

def maxSum(arr, n):
    # compute sum of all element
    cum_sum = 0
    for x in range(len(arr)):
        cum_sum += arr[x]
    
    # compute sum of i * arr[i] for initial configuration
    curr_val = 0
    for x in range(len(arr)):
        curr_val += x * arr[x]
    
    # initial result
    res = curr_val

    # compute value for other iterations
    for x in range(1, len(arr)):
        # Compute next value using previous value
        next_val = curr_val - ( cum_sum - arr[x-1] ) + ( arr[x-1] * (n-1) )

        # update current value
        curr_val = next_val

        # update result if required
        res = max(res, next_val)
    
    return res

print(maxSum([8,3,1,2], len([8,3,1,2])))
print(maxSum([3,2,1], len([3,2,1])))

# Time Complexity: O(n)
