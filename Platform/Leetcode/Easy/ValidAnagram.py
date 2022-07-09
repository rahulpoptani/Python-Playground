# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Input: s = "anagram", t = "nagaram"
# Output: true 
# Input: s = "rat", t = "car"
# Output: false

# Anagram = Two words are anagram if both have same characters

# Approach 1 - Sort both the string and compare

def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

print(isAnagram('anagram', 'nagaram'))

print(isAnagram('rat', 'cat'))