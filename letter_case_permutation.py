# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:55:19 2019

Leetcode: Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Time Complexity: O(n), one loop to go through the string
Space Complexity: O(m^2), where m is the number of letters in string S

@author: bohan

"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        permDict = {}
        lastLetterIndex = 0
        
        if not S[0] in '0123456789':
            permDict[lastLetterIndex] = [S[0].upper(), S[0].lower()]
        else:
            permDict[lastLetterIndex] = [S[0]]
        
        print(permDict)
        for i in range(1, len(S)):
            if not S[i] in '0123456789':
                lastLetterIndex += 1
                permDict[lastLetterIndex] = []
                for item in permDict[lastLetterIndex-1]:
                    permDict[lastLetterIndex].append(item + S[i].upper())
                    permDict[lastLetterIndex].append(item + S[i].lower())
            else:
                temp = []
                for item in permDict[lastLetterIndex]:
                    temp.append(item + S[i])
                permDict[lastLetterIndex] = temp
        
        return permDict[lastLetterIndex]