
from array import array

# 'i' means signed int
arr = array('i', [1,2,3])

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()

# Print all elements
print_array(arr)

# Append value
arr.append(6)
arr.append(6)
print_array(arr)

# Insert 5 and 2nd position
arr.insert(2, 5)
print_array(arr)

# pop: removes the element from the position, by default removes from last position
arr.pop(2)
print_array(arr)

# remove: Removed the 1st occurrence of the value given
arr.remove(6)
print_array(arr)

# index: returns index of the first occurence of the element
element = 3
print('Element {} found at Index: {}'.format(element,arr.index(element)))

# reverse: reverse the array inplace
arr.reverse()
print_array(arr)