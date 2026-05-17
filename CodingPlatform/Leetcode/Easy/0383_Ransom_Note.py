'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true 
'''

from Common.Tags import GRIND_75, STRING, HASHMAP
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    
    ransomNoteCount = Counter(ransomNote)
    magazineCount = Counter(magazine)
    
    for char, count in ransomNoteCount.items():
        if magazineCount[char] < count:
            return False
            
    return True

# Time Complexity: O(n + m) where n is the length of ransomNote and m is the length of magazine
# Space Complexity: O(n + m) for the two Counter objects

# Tests
print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
print(canConstruct("dd", "aab"))