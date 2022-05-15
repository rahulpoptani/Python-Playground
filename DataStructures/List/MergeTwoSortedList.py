
def merge_lists(lst1, lst2):
    x = 0
    y = 0
    while (x < len(lst1) and y < len(lst2)):
        # if current element if list 1 is greater than current element of list 2
        if (lst1[x] > lst2[y]):
            # insert current element of list 2 into list 1 and extend the pointer on both lists
            lst1.insert(x, lst2[y])
            x += 1
            y += 1
        else:
            x += 1
    # if list2 have more elements to traverse, then add them into list 1
    if (y < len(lst2)):
        lst1.extend(lst2[y:])
    return lst1

list1 = [1,3,4,8,9]  
list2 = [2,5,6,7]
mergelist = merge_lists(list1, list2)
print(mergelist)

# Time Complexity:
# Since both list are traversed the time complexity is O(m(m+n)) where m and n are length of list
# If both list were traversed saperately in such case it will be O(m+n)
# In worst-case, 2nd list have all elements smaller than 1st list, in this case it will be O(mn)