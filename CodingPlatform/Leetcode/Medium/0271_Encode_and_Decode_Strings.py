'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
'''

from typing import List
from Common.Tags import STRING, BLIND75


def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s: str) -> List[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return res

# Example usage:
encoded = encode(["hello", "world"])
print(f"Encoded: {encoded}")
decoded = decode(encoded)
print(f"Decoded: {decoded}")