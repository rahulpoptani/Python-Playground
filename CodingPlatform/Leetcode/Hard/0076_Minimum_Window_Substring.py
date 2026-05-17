'''
Given two strings 's' and 't' of lengths m and n respectively, return the minimum window 
substring of 's' such that every character in 't' (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string. 
'''

from Common.Tags import STRING, HASHMAP, SLIDING_WINDOW
from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)
    have, required = 0, len(need)  # distinct chars that need to be satisfied
    
    window = {}
    best = ""
    l = 0

    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        
        # Did this addition satisfy a character's requirement?
        if c in need and window[c] == need[c]:
            have += 1
        
        # Shrink from left while window is valid
        while have == required:
            # Update best
            if not best or (r - l + 1) < len(best):
                best = s[l:r+1]
            
            # Remove leftmost char
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    return best

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(float("infinity"))

