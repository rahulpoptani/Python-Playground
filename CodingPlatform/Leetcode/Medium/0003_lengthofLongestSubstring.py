'''
Find the longest substring without repeating character
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Input: s = "dvdf"
Output: 3
Explanation: The answer is "vdf", with the length of 3.
'''


def lengthOfLongestSubstring(s: str) -> int:
    res = set()
    left = 0
    maxchar = 0

    for right in range(len(s)):
        while(s[right] in res):
            res.remove(s[left])
            left += 1
        res.add(s[right])
        maxchar = max(maxchar, right - left + 1) # instead of right-left+1, we can also use len(res), but the time complexity to calculate the length would be an overhead:
    
    return maxchar


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('dvdf'))