def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(right_rotate([10,20,30,40,50],2))
print(right_rotate([],2))

# Time Complexity: Entire list is sliced, O(n)