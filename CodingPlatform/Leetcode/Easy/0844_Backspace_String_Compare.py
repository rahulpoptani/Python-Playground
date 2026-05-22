'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b". 
'''

from Common.Tags import STRING, STACK

def backspaceCompare(s: str, t: str) -> bool:
    def getString(string: str) -> str:
        result = []
        for char in string:
            if char == '#':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)
    return getString(s) == getString(t)

# Test cases
print(backspaceCompare("ab#c", "ad#c"))  # Output: True
print(backspaceCompare("ab##", "c#d#"))  # Output: True
print(backspaceCompare("a#c", "b"))      # Output: False