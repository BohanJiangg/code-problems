# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 06:27:43 2018
Leetcode: Excel Sheet Column Number
Time complexity: O(n), where n is the length of the column number string
Space Complexity: O(1)
@author: bohan
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cumul = 0
        idx = 0
        for i in range(len(s) - 1, -1, -1):
            num = ord(s[i]) - 64
            
            cumul += num * (26 ** idx)
            idx += 1
        
        return cumul