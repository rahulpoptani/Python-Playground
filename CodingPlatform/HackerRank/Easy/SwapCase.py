'''
Convert all lower case to upper and vice versa
Input:
------
Www.HackerRank.com
Output:
--------
wWW.hACKERrANK.COM
'''

def swap_case(s):
    newString = ''
    for x in s:
        diff = 0
        if ord(x) >= 65 and ord(x) <= 90:
            diff = abs(65 - ord(x))
            newString += chr(97 + diff)
            continue
        if ord(x) >= 97 and ord(x) <= 122:
            diff = abs(97 - ord(x))
            newString += chr(65 + diff)
            continue
        newString += x
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)