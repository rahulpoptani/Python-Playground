# Rearange the list - all negatives numbers appears on left and positive on right. Order is not important

def rearrange(lst):
    end=0
    lst2 = []
    for x in lst:
        if x < 0:
            lst2.insert(0, x)
            end += 1
        else:
            lst2.insert(end, x)
            end += 1
    return lst2

def rearrange2(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


print(rearrange([10,-1,20,4,5,-9,-6]))
print(rearrange2([10,-1,20,4,5,-9,-6]))

# Time Complexity: O(n)
# Iterate over list once or twice, in both case time complexity is same