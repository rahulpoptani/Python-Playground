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

    for x in s:
        
        if x not in res:
            res.add(x)
            maxchar = max(maxchar, len(res))
        else:
            while(x in res):
                res.remove(s[left])
                left += 1
            res.add(x)
    
    print(f'Length of longest substring from string: {s} is : {maxchar}')


lengthOfLongestSubstring('pwwkew')
lengthOfLongestSubstring('bbbbb')
lengthOfLongestSubstring('abcabcbb')
lengthOfLongestSubstring('dvdf')