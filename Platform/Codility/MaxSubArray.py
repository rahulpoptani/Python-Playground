# Find max subarray in an array
# In an array [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
# Max subarray is [4, -3, 2, 7] with sum 10

def max_subarray(lst):
    global_sum = 0
    local_sum = 0
    for x in range(len(lst)):
        if x == 0:
            global_sum = local_sum = lst[x]
        else:
            local_sum = max(local_sum, local_sum + lst[x])
            if local_sum > global_sum:
                global_sum = local_sum
            else:
                local_sum = lst[x]
    print(f'Max Sub List: {global_sum}')

arr = [-4,2,-5,1,2,3,6,-5,1]
max_subarray(arr)

