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