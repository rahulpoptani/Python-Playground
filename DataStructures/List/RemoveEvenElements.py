def remove_even(lst):
    for x in lst.copy():
        if x % 2 == 0:
            lst.remove(x)
    return lst


my_list = [1,2,4,5,10,6,3]
print(remove_even(my_list))

# without list copy output: [1, 4, 5, 6, 3]
# with list copy outut: [1, 5, 3]
# Reason: when checking for 2nd index which is 2, it would remove 2nd index and the new list would be
# [1,4,5,10,6,3] and because 2nd index is already looped over it would move to 3rd index which is 5 and miss the shifted 2nd index
# this will give wrong output

# Instead of above, the shorter solution would be more cleaner
def remove_even2(lst):
    return [x for x in lst if x % 2 != 0]

my_list2 = [1,2,4,5,10,6,3]
print(remove_even2(my_list))

# Time complexity: Since the entire list was iterated the time complexity is O(n)
