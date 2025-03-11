from Common.Tags import ARRAY
import sys

def find_second_maximum(lst):
    max_element = sys.float_info.min
    second_max_element = sys.float_info.min
    for x in lst:
        if x > max_element:
            second_max_element = max_element
            max_element = x
        elif x > second_max_element and x < max_element:
            second_max_element = x
    return second_max_element

print(find_second_maximum([9,2,3,6]))

# Traversing the list one time.
# Time Complexity: O(n)

# Another Approach: Sort the list and return element at Index -2
# Time Complexity: Sorting will take O(nlogn) and accessing element in constant time. Hence overall => O(nlogn)

# Another Approach: Traversing the list twice. First identity Max element. In 2nd traversor find max element not grater than 1st max element
# Time Complexity: O(n)