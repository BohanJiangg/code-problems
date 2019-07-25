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

Time Complexity O(n), 
Space Complexity: O(1), 
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

        wordDict = {}
        minLen = len(words[0])
        for word in words:
            length = len(word)
            if length < minLen:
                minLen = length
            if not length in wordDict:
                wordDict[length] = [word]
            else:
                wordDict[length].append(word)
        
        count = 0
        currChain = set()
        for word in wordDict[minLen]:
            currChain.add(word)
        minLen += 1

        while minLen in wordDict and currChain:
            count+=1
            for i in range(len(currChain)):
                curr = currChain.pop()
                for word in wordDict[minLen]:
                    temp = word
                    for ch in curr:
                        if ch in word:
                            word = word.replace(ch, '')
                    if len(word) ==1:
                        currChain.add(temp)
                        
            minLen += 1
            
        
        return count+1




'''
Sort the words by word's length. (also can appply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.

def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())

'''

        