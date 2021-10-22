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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                print(r, l, charSet)
            charSet.add(s[r])
            res = max(res, r - l + 1)
            print(r, l, charSet)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))