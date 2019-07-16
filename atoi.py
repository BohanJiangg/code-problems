# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:23:57 2019
Leetcode:  String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Time Complexity O(n), iterate through string once
Space Complexity: O(n), need to keep track of string of numbers 
@author: bohan
"""

class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        
        string = string.strip()
        if not string:
            return 0
        
        nums = '0123456789'
        flag = 1
        toRet = '0'

        first = string[0]

        if first == '-':
            flag = -1
        elif first == '+':
            flag = 1
        elif first in nums:
            toRet += first
        else:
            return 0
       
        for i in range(1, len(string)):
            ch = string[i]
            if ch in nums:
                toRet += ch
            else:
                toRet = int(toRet) * flag
                if toRet < -2**31:
                     return -2**31
                elif toRet > (2**31)-1:
                     return (2**31)-1
                else:
                     return toRet
    
        toRet = int(toRet) * flag
        if toRet < -2**31:
            return -2**31
        elif toRet > (2**31)-1:
            return (2**31)-1
        else:
            return toRet
       
      