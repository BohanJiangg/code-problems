# -*- coding: utf-8 -*-
"""
Created on August 22 2019
Leetcode: Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "abababa"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        if not S:
            return ''
        count = collections.Counter(list(S))
        length = len(S)
        if length % 2 == 0 and max(count.values()) >= length // 2:
            return ''
        elif max(count.values()) > (length // 2)+1:
            return ''
        else:
            # reorganizable
            left = 1
            right = length-1
            S = list(S)
            while left < right:
                while left < right and  S[left-1] != S[left]:
                    left += 1
                while left < right-1 and S[right-1] != S[right]:
                    right -= 1
                S[left], S[right] = S[right], S[left]

            return ''.join(S)
            