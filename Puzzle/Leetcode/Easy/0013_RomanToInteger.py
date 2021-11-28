'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Input: s = "III"
Output: 3

Input: s = "IV"
Output: 4

Input: s = "IX"
Output: 9

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4
'''

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, "C": 100, 'D': 500, 'M': 1000}

def romanToInt(s: str) -> int:
    prev = 0
    curr = 0
    total = 0

    for x in s:
        curr = dict[x]
        if curr > prev:
            total += (curr + (-2 * prev))
        else:
            total += curr
        prev = curr
    return total


print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))