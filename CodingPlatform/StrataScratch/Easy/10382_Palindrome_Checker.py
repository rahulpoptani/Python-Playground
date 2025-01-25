'''
Check if a given input is a palindrome.

Test Case #1
Input: "A man, a plan, a canal, Panama"
Output: false
Description: This test case checks the functions ability to handle input with punctuation and spaces. Even though the phrase is often regarded as a palindrome, the spaces and punctuation make it not a strict palindrome according to the algorithm.

Test Case #2
Input: "Able was I, ere I saw Elba"
Output: false
Description: Testing the function with a famous palindrome phrase ignoring spaces and punctuation. The algorithm is expected to fail as it does not preprocess to ignore non-alphabetic characters.

Test Case #3
Input: "Ablewasiereisawelba"
Output: true
Description: This case ensures that the function works correctly for a fully lowercase version of the palindrome without spaces or punctuation, thus requiring a proper check for character-by-character mirroring.
'''

def is_palindrome(s):
    """ 
    :type s: str
    :rtype: bool
    """
    i, j = 0, (len(s) - 1)
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Time: O(n)
# Space: O(1)

# Test Cases
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Able was I, ere I saw Elba"))
print(is_palindrome("Ablewasiereisawelba"))