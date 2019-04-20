# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:55:55 2019

CTCI: Problem 1.4 - Palindrome Permutations
Time Complexity: O(n), loop through string to put into stringDict, then loop through stringDict
Space Complexity: O(n), copy string to all lowercase, new dictionary to store counts of each character

@author: bohan
"""


'''
Function that identifies if string is permutation of a palindrome
Ignores all non-letter characters and casing
'''
def isPermutationOfPalindrome(string):
    string = string.lower()
    
    stringDict = {} 
    for ch in string:
        if ch.isalpha():
            if not ch in stringDict:
                stringDict[ch] = 1
            else:
                stringDict[ch] += 1
    

    isSingle = 0
    for key in stringDict:
        if stringDict[key] % 2 != 0:
            isSingle += 1
            if isSingle > 1:
                return False
    
    return True



if __name__ == '__main__':
    print(isPermutationOfPalindrome("Tact Coa"))
    print(isPermutationOfPalindrome("CCooAA"))
    print(isPermutationOfPalindrome('dRAdff'))