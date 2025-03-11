from Common.Tags import ARRAY

def find_minimum(arr):
    if (len(arr) <= 0):
        return None
    minele = arr[0]
    for x in arr[1:]:
        if x < minele:
            minele = x
    return minele

print(find_minimum([9,2,3,6]))
print(find_minimum([4,2,1,5,0]))

# Time Complexity: The list is traverse one time, O(n)

# Another Approach where you can sort the list and return first element from sorted list. 
# Sorting will take O(nlogn), returning from index takes constant time. Overall complexity O(nlogn)