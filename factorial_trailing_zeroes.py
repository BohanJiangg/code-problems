# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:18:00 2019

CTCI: Problem 16.5 - Factorial Zeroes
Leetcode: Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Time Complexity: O(n), grows with exponent of 5 
Space Complexity: O(1), need two constants. 

@author: bohan

"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        
        numZeroes = 0
        # zeroes appear by counting the number of 5s in the prime factors of n 
        # need to consider exponents of 5: 5^2 = 25, 5^3 = 125 and get these extra zeroes. 
        i = 5
        while (n/i>=1):
            numZeroes += int(n/i)
            i*=5
        
        
        return (numZeroes)
        