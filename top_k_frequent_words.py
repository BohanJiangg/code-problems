# -*- coding: utf-8 -*-
"""
Created on August 6 2019
Leetcode: Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Time Complexity O(n log n), need to sort elements by frequency and by alphabetical order
Space Complexity: O(n), creates a copy of words
@author: bohan
"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        
        word_dict = collections.Counter(words)

        candidates = word_dict.keys()
        candidates.sort(key = lambda w: (-word_dict[w], w))
    
        return candidates[:k]

        