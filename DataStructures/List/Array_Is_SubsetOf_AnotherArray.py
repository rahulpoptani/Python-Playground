
def isSubset(arr1,arr2):
    s = set()
    for x in arr1:
        s.add(x)
    size = len(s)
    for x in arr2:
        s.add(x)
    if len(s) == size:
        return True
    else: return False

# Time Complexity O(m+n)

arr1 = [ 11, 1, 13, 21, 3, 7 ]
arr2 = [ 11, 3, 7, 1 ]

print(isSubset(arr1,arr2))
print(isSubset(arr2,arr1))