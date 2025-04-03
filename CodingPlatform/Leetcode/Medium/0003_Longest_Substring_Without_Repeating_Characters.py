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

'''
Time Complexity: O(n)
    The time complexity of the solution is O(n), where n is the length of the input string s.
    The right pointer iterates through the string once, and for each character, the left pointer may also move forward, but each character is added to and removed from the set res at most once.
    This means that the while loop inside the for loop runs at most n times in total, as each character is processed only once by both the right and left pointers.
    Thus, the overall time complexity is O(n).

Space Complexity: O(k)
    The space complexity of the solution is O(k), where k is the size of the character set used in the input string s.
    The set res is used to store the characters of the current substring without repeating characters. In the worst case, the size of res can grow to the size of the entire character set of the input string.
    For example, if the input string contains all unique characters, the size of res will be equal to the length of the string s.
    If the input string contains only lowercase English letters, k would be at most 26. If the input string contains all possible Unicode characters, k could be much larger.
    Thus, the space complexity is O(k), where k is the size of the character set in the input string.
'''