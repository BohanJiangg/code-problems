# -*- coding: utf-8 -*-
"""
Created on July 23 2019
Leetcode: Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example:
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

Time Complexity O(n log n), need to sort words 
Space Complexity: O(n), need dp dict to store values we've seen before 
@author: bohan
"""

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        if not words:
            return 0

        dp = {}
        for word in words:
            dp[word] = 1
        
        for word in sorted(words, key=len)[::-1]:
            for i in range(len(word)):
                mod = word[:i] + word[i+1:]
                if mod in dp:
                    dp[mod] = max(dp[mod], 1+dp[word])
        
        return max(dp.values())