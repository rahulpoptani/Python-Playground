'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2 
    Since 2 has only one digit, return it.
Example 2:
    Input: num = 0
    Output: 0
'''

from Common.Tags import SIMULATION

def addDigits(num: int) -> int:
    if num == 0:
        return 0
    else:
        # This formula is derived from the digital root concept, which states that the result of repeatedly summing the digits of a number until a single digit is obtained can be calculated using modulo 9.
        return 1 + (num - 1) % 9 # return num % 9 or 9

# Example usage:
print(addDigits(38))  # Output: 2
print(addDigits(0))   # Output: 0
