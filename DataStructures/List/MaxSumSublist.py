def find_max_sum_sublist(lst): 
    if len(lst) < 1:
        return 0
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
    return global_sum


print(find_max_sum_sublist([-4,2,-5,1,2,3,6,-5,1]))

# Algorithm Used: Kadane's Algorithm - Dynamic Programming Approach
# Time Complexity: O(n)
# Memory Complexity: O(1)

