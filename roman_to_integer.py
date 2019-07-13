# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:03:36 2019

Leetcode: Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


Time Complexity: O(n), iterate through array once 
Space Complexity: O(n), 

@author: bohan

"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        dic = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        
        length = len(s)
        idx = 0
        toRet = 0
        
        while idx < length:
            char = s[idx]
            
            if char == 'I':
                if idx +1 < length and s[idx+1] == 'V':
                    toRet += dic[char + s[idx+1]]
                    idx += 2
                elif idx +1 < length and s[idx+1] == 'X':
                    toRet += dic[char + s[idx+1]]
                    idx += 2
                else:
                    toRet += dic[char]
                    idx += 1
            elif char == 'X':
                if idx +1 < length and s[idx+1] == 'L':
                    toRet += dic[char + s[idx+1]]
                    idx += 2
                elif idx +1 < length and s[idx+1] == 'C':
                    toRet += dic[char + s[idx+1]]
                    idx += 2
                else:
                    toRet += dic[char]
                    idx += 1
            elif char == 'C':
                if idx +1 < length and s[idx+1] == 'D':
                    toRet += dic[char + s[idx+1]]
                    idx += 2
                elif idx +1 < length and s[idx+1] == 'M':
                    toRet += dic[char + s[idx+1]]
                    idx += 2
                else:
                    toRet += dic[char]
                    idx += 1
            else:
                toRet += dic[char]
                idx += 1
        
        return toRet
    
    