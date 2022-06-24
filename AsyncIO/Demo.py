#!/bin/python3

import math
import os
from pydoc import plain
import random
import re
import sys



def findMaxCharacterAscii(str):
    maxcharasci = 97
    for x in str:
        maxcharasci = max(maxcharasci, ord(x))
    print('returning max as ', maxcharasci)
    return maxcharasci
    
def breakPalindrome(palindromeStr):
    minlist = []
    l = len(palindromeStr)//2
    first = palindromeStr[0:l]
    second = palindromeStr[l:]
    print(first, second)
    totalMaxCharacterAscii = findMaxCharacterAscii(palindromeStr)
    firstMaxCharacterAscii = findMaxCharacterAscii(first)
    secondMaxCharacterAscii = findMaxCharacterAscii(second)
    print(firstMaxCharacterAscii, secondMaxCharacterAscii)
    if totalMaxCharacterAscii > 97:
        while firstMaxCharacterAscii > 97:
            currentString = ''
            for x in range(len(first)):
                print(x)
                if ord(first[x]) == firstMaxCharacterAscii:
                    currentString += chr(ord(first[x])-1)
                    currentString += first[x+1:]
                    print(currentString)
                    break
                else:
                    currentString += first[x]
            minlist.append(currentString)
            firstMaxCharacterAscii = findMaxCharacterAscii(currentString)
            first = currentString
        while firstMaxCharacterAscii > 97:
            currentString = ''
            for x in range(len(first)):
                print(x)
                if ord(first[x]) == firstMaxCharacterAscii:
                    currentString += chr(ord(first[x])-1)
                    currentString += first[x+1:]
                    print(currentString)
                    break
                else:
                    currentString += first[x]
            minlist.append(currentString)
            firstMaxCharacterAscii = findMaxCharacterAscii(currentString)
            first = currentString

    else: return 'IMPOSSIBLE'
    while findMaxCharacterAscii > 97:



def breakPalindrome2(palindromeStr):
    # Write your code here
    processString = palindromeStr
    minlist = []
    maxCharacterAscii = findMaxCharacterAscii(processString)
    count = 0
    if maxCharacterAscii > 97:
        while maxCharacterAscii > 97:
            currentString = ''
            for x in range(len(processString)):
                print(x)
                if ord(processString[x]) == maxCharacterAscii:
                    currentString += chr(ord(processString[x])-1)
                    currentString += processString[x+1:]
                    print(currentString)
                    break
                else:
                    currentString += processString[x]
            minlist.append(currentString)
            print(minlist)
            maxCharacterAscii = findMaxCharacterAscii(currentString)
            processString = currentString

        print(minlist)
        return min(minlist)
    else:
        return 'IMPOSSIBLE'
            
        
            
breakPalindrome('bab')