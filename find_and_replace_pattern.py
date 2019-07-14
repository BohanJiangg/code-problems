# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 08:39:06 2019
Leetcode: Find and Replace Pattern

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Time Complexity O(n*m), need to go through every char (m) of words list (n) 
Space Complexity: O(m), need to keep 2 dictionaries for every word 
@author: bohan
"""


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        if not pattern or not words:
            return []
        
        
        outputList = []
        
        for word in words:
            wordToPattern = {}
            patternToWord = {}
            if len(word) == len(pattern):
                match = True
                for i in range(len(word)):
                    patternChar = pattern[i]
                    wordChar = word[i]
                    
                    if patternChar in patternToWord and wordChar in wordToPattern:
                        if not wordToPattern[wordChar] == patternChar or not patternToWord[patternChar] == wordChar:
                            match = False
                            break
                    elif not patternChar in patternToWord and not wordChar in wordToPattern:
                        wordToPattern[wordChar] = patternChar
                        patternToWord[patternChar] = wordChar
                    else:
                        match = False
                        break
                    
                if match == True:
                    outputList.append(word)
        
        return outputList