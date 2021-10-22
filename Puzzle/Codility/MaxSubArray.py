# Find max subarray in an array
# In an array [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
# Max subarray is [4, -3, 2, 7] with sum 10

def max_subarray(arr):
    global_max = 0
    local_max = 0
    for x in range(len(arr)):
        if x == 0:
            global_max = local_max = arr[x]
        else:
            local_max = max(arr[x], local_max + arr[x])
            print('Itr: {} New local max {}'.format(x, local_max))
            if local_max > global_max:
                global_max = local_max
                local_max = arr[x]
                print('New global and local max {}, {}'.format(global_max, local_max))
    print('Maximum Sub Array Sum = {}'.format(global_max))

arr = [1,2,3,-4,5,6]
max_subarray(arr)

