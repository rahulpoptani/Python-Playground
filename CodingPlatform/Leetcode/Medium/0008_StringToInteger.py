'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer

Input: s = "42"
Output: 42

Input: s = "   -42"
Output: -42

Input: s = "4193 with words"
Output: 4193

Input: s = "words and 987"
Output: 0

Input: s = "-91283472332"
Output: -2147483648
Since -91283472332 is less than the lower bound of the range [-2 (power 31), 2 (power 31) - 1], the final result is clamped to -231 = -2147483648.
'''

def myAtoi(s: str) -> int:
    str = s.strip()
    negative = False
    out = 0

    if not str:
        return 0
    
    if str[0] == '-':
        negative = True
        str = str[1:]
    elif str[0] == '+':
        negative = False
    elif not str[0].isnumeric:
        return 0
    
    try:
        out = int(str[0])
    except ValueError:
        return 0
    
    for x in range(1, len(str)):
        if str[x].isnumeric():
            out = out*10 + int(str[x])
            if not negative and out > 2147483647:
                return 2147483647
            if negative and out > 2147483647:
                return -2147483648
        else:
            break
    
    if not negative: return out
    else: return -out


print(myAtoi(s = "42"))
print(myAtoi(s = "   -42"))
print(myAtoi(s = "4193 with words"))
print(myAtoi(s = "words and 987"))
print(myAtoi(s = "-91283472332"))