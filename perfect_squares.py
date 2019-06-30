# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:31:44 2019

Leetcode: Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Time Complexity: O()
Space Complexity: O(), 

@author: bohan

"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        largestPS = int(n**(1/2))
        
        if largestPS ** largestPS == n:
            return 1
        
        least = n
        
        
        
        while largestPS > 1:
            currSum = largestPS ** largestPS
            remainder = n - currSum
            largestPS = int(remainder**(1/2))
            if largestPS == 1:
            
            
        
        
        
        
        