'''
Count the number of words in a given sentence.

Test Case #1
Input: "The quick brown fox jumps over a lazy dog"
Output: 9
Description: This test case evaluates the function"s ability to count words in a common English sentence without punctuation.

Test Case #2
Input: "Hello, world! This-is_a test."
Output: 4
Description: This test checks the function"s capability to correctly split and count words in a sentence containing various punctuation marks and separators.

Test Case #3
Input: " Multiple spaces between some of the words "
Output: 7
Description: This case verifies how the function handles sentences with irregular spacing, including leading and trailing spaces.
'''

def count_words(sentence):
    """ 
    :type sentence: str
    :rtype: int 
    """
    return len(list(map(lambda x: x.strip(), sentence.split())))

# Test Cases
print(count_words("The quick brown fox jumps over a lazy dog")) # 9
print(count_words("Hello, world! This-is_a test.")) # 4
print(count_words(" Multiple spaces between some of the words ")) # 7

# Time Complexity: O(n)
# Space Complexity: O(n)
# Explain time complexity
# The time complexity of this function is O(n) because it splits the input sentence into words and then counts the number of words. 
# The split operation takes O(n) time, where n is the number of characters in the sentence. 
# The count operation also takes O(n) time because it iterates over the list of words to determine its length. Therefore, the overall time complexity of the function is O(n).
