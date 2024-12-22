'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
'''

from collections import Counter

def minSteps(s: str, t: str) -> int:
    count_s = Counter(s)
    count_t = Counter(t)

    steps = 0
    for char in count_s:
        value = count_s.get(char, 0) - count_t.get(char, 0)
        if value > 0:
            steps += value

    return steps

print(minSteps(s = "bab", t = "aba"))
print(minSteps(s = "leetcode", t = "practice"))
print(minSteps(s = "anagram", t = "mangaar"))