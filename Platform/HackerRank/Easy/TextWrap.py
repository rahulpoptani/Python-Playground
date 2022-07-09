'''
Given a String S, Wrap into paragraph with width W
Input:
-------
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Output:
--------
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

import textwrap

def wrap(string, max_width):
    wrapList = textwrap.wrap(string, max_width)
    return '\n'.join(wrapList)

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',3))

