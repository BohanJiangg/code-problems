# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:02:27 2019
Leetcode: Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Time Complexity O(1), one calculation 
Space Complexity: O(1), one calculation
@author: bohan
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        
        return x**n