# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:19:07 2019

CTCI: Problem 16.18 - Pattern Matching
Leetcode: Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.


Time Complexity: O(n^2), need to loop through pattern and also check dict values 
Space Complexity: O(n), dict to keep track of pattern and words.  

@author: bohan

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        
        """
        
        
        patternDict = {}
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        
        
        for i in range(len(pattern)):
            
            if pattern[i] in patternDict and patternDict[pattern[i]] != words[i]:
                return False
            elif not pattern[i] in patternDict:
                if not words[i] in patternDict.values():
                    patternDict[pattern[i]] = words[i]
                else:
                    return False
        
        return True