'''
Find the maximum value, its key, and index from a dictionary. Assume all values are unique.

Test Case #1
Input: {"a": 4, "b": 10, "c": 6, "d": 8}
Output: [10, "b", 1]
Description: This test case checks that the function correctly identifies the maximum value from a set of mixed integers and returns its corresponding key and index.

Test Case #2
Input: {"pear": 75, "apple": 100, "peach": 150, "banana": 50}
Output: [150, "peach", 2]
Description: This test case challenges the algorithm""s ability to find the maximum value in a dictionary with string keys, verifying correct identification of both the key and its index.

Test Case #3
Input: {"cat": 3, "dog": 7, "monkey": 5, "giraffe": 9, "elephant": 2}
Output: [9, "giraffe", 3]
Description: This case evaluates the function"s performance with multiple entries where the maximum value is neither at the start nor the end of the dictionary.
'''

def find_max_value(dictionary):
    """ 
    :type dictionary: dict
    :rtype: tuple
    """
    max_value, max_key, max_index = None, None, None
    for i, (key, value) in enumerate(dictionary.items()):
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
            max_index = i
    return [max_value, max_key, max_index]

# Time: O(n)
# Space: O(1)

# Test Cases
print(find_max_value({"a": 4, "b": 10, "c": 6, "d": 8})) # [10, "b", 1]
print(find_max_value({"pear": 75, "apple": 100, "peach": 150, "banana": 50})) # [150, "peach", 2]
print(find_max_value({"cat": 3, "dog": 7, "monkey": 5, "giraffe": 9, "elephant": 2})) # [9, "giraffe", 3]
print(find_max_value({})) # [None, None, None]
