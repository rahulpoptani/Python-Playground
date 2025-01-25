'''
Find unique values in a given list.

Test Case #1
Input: [5, 1, -1, 2, 5, 1, 2]
Output: [5, 1, -1, 2]
Description: This test case checks the function ability to handle a list with positive and negative numbers and repeated elements, ensuring only the first occurrences are retained in the order they appear.

Test Case #2
Input: [0, -1, 0, 0, 2, 2, -3, -3, -3]
Output: [0, -1, 2, -3]
Description: The function is tested for its capability to handle zero values and negative numbers while filtering out consecutive duplicates.

Test Case #3
Input: [-100, 100, 200, -100, 500, 100]
Output: [-100, 100, 200, 500]
Description: This case assesses the algorithms performance on a range of large positive and negative values, with duplicates interspersed in the sequence.
'''

def non_duplicate(input):
    """ 
    :type input: List[int]
    :rtype: List[int]
    """
    seen = set()
    result = []
    for x in input:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of the input list
# The function iterates through the input list once, and the set is used to store the unique elements.
# The space complexity is O(n) because the set can contain at most n elements.

# Test cases
print(non_duplicate([5, 1, -1, 2, 5, 1, 2])) # [5, 1, -1, 2]
print(non_duplicate([0, -1, 0, 0, 2, 2, -3, -3, -3])) # [0, -1, 2, -3]
print(non_duplicate([-100, 100, 200, -100, 500, 100])) # [-100, 100, 200, 500]
