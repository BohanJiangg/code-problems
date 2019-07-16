# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:23:29 2019
Leetcode: Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        