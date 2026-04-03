'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
        
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
        
    return list(groups.values())

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(strs = [""]))
print(groupAnagrams(strs = ["a"]))
print(groupAnagrams(strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
