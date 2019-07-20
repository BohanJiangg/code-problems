# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:26:03 2019

Leetcode: Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Time Complexity O(log n), continously loop and divide by 4 
Space Complexity: O(1), operations in place
@author: bohan
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num < 0:
            return False
        
        if num == 0:
            return False
        if num == 1:
            return True
        num = float(num)
        while num.is_integer():
            num = num / 4
            if num == 1:
                return True
        return False