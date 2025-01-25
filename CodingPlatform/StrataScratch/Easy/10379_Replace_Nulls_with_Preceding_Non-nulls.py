'''
Given a list of values containing NULLs, for every null value, replace it with its preceding non-null value.

Test Case #1
Input: [null, 5, null, 8, null, null, 3, null]
Output: [null, 5, 5, 8, 8, 8, 3, 3]
Description: This test case assesses the function’s ability to handle lists with null values at the beginning and multiple consecutive null values.

Test Case #2
Input: [12, 14, null, null, 7, null, 19, null, null, 23]
Output: [12, 14, 14, 14, 7, 7, 19, 19, 19, 23]
Description: This test case examines how the function handles several sequences containing non-null elements interspersed with multiple null values.

Test Case #3
Input: [null, null, 6, null, 5, null, null, 2, null, 3]
Output: [null, null, 6, 6, 5, 5, 5, 2, 2, 3]
Description: This test case checks the function"s ability to process lists starting with multiple null values and having non-null values scattered through the list.
'''

def replace_null_values(lst):
    """ 
    :type lst: List[Union[int, None]]
    :rtype: List[Union[int, None]]
    """
    for i in range(1, len(lst)):
        if lst[i] is None:
            lst[i] = lst[i-1]
    return lst

# Time: O(n)
# Space: O(1)

# Unit Test
print(replace_null_values([None, 5, None, 8, None, None, 3, None])) # [None, 5, 5, 8, 8, 8, 3, 3]
print(replace_null_values([12, 14, None, None, 7, None, 19, None, None, 23])) # [12, 14, 14, 14, 7, 7, 19, 19, 19, 23]
print(replace_null_values([None, None, 6, None, 5, None, None, 2, None, 3])) # [None, None, 6, 6, 5, 5, 5, 2, 2, 3]
print(replace_null_values([None, None, None, None, None, None, None, None, None, None])) # [None, None, None, None, None, None, None, None, None, None]
print(replace_null_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(replace_null_values([None, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [None, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(replace_null_values([1, 2, 3, 4, 5, 6, 7, 8, 9, None])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
print(replace_null_values([1, 2, 3, 4, 5, 6, 7, 8, None, None])) # [1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
print(replace_null_values([None, None, None, 10])) # [None, None, None, 10]
print(replace_null_values([None, None, 9, 10])) # [None, None, 9, 10]
