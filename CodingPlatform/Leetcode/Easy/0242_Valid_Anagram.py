'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

from Common.Tags import STRING, HASHMAP, BLIND75

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False
    
    dictS = {}
    dictT = {}
    
    for i in range(len(s)):
        dictS[s[i]] = 1 + dictS.get(s[i],0)
        dictT[t[i]] = 1 + dictT.get(t[i],0)
    
    for x in dictS.keys():
        if dictS[x] != dictT.get(x,0): 
            return False
    
    return True

from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    return len(s) == len(t) and Counter(s) == Counter(t)

print(isAnagram('anagram', 'nagaram'))
print(isAnagram('rat', 'car'))