# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:13:18 2019

CTCI: Problem 1.2 - Check Permutations
Time Complexity: O(str1) time, loop through str1 to store in strDict, then loop through str2 to check (but never longer than str1)
Space Complexity: O(str1) since need a dict potentially as long as str1

@author: bohan
"""


''' 
Function that checks if one string is the permutation of another
'''
def checkPermutation(str1, str2):
    strDict = {}
    
    #Optimization: return false if not same length
    if (len(str1) != len(str2)):
        return False
    
    # Count and store all occurences of str1 into dict
    for ch in str1:
        if ch in strDict:
            strDict[ch] += 1
        else:
            strDict[ch] = 1
    
    # Loop through str2 and count and match each char with those
    # stored in strDict
    for ch in str2:
        if not ch in strDict:
            return False
        else:
            strDict[ch] -= 1
            if strDict[ch] < 0:
                return False
    
    return True
    
    
if __name__ == '__main__':
    print(checkPermutation('hello', 'olleh'))
    print(checkPermutation('hello', 'solleh'))
    print(checkPermutation('sd sd', 'sd  sd'))
    