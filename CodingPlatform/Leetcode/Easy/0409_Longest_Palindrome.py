'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''
from Common.Tags import STRING, HASHMAP

def longestPalindrome(s: str) -> int:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    odd_count_found = False

    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_count_found = True

    if odd_count_found:
        length += 1

    return length