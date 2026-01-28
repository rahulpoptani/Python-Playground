'''
Write a function to find the longest common prefix string amongst an array of strings.

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
from Common.Tags import ARRAY, STRING
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Time Complexity:
        O(S) where S is the sum of all characters in all strings.
        In the worst case, all strings are identical, and we iterate through every character
        of the first string while checking all other strings.
        More precisely: O(n * m) where n is the number of strings and m is the length of the
        shortest string.

    Space Complexity:
        O(1) if we don't count the output string.
        O(m) if we count the output string, where m is the length of the common prefix.
    """
    prefix = ""
    pos = 0
    while pos < len(strs[0]):
        ele = strs[0][pos]
        for x in strs:
            if pos >= len(x) or x[pos] != ele:
                return prefix
        prefix += ele
        pos += 1
    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["aaa","aaa","aaa"]))
print(longestCommonPrefix(["ab","a"]))