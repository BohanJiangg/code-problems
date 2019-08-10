# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:06:13 2019

Leetcode: Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.


Time Complexity: O(n^2), solution by iterating over words in wordDict and every character in s  
Space Complexity: O(n), need a boolean array to memoize found words

@author: bohan
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (d[i-len(word)] or i-len(word) == -1):
                    d[i] = True
        
        return d[-1]
        