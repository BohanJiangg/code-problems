# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:31:44 2019

Leetcode: Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Time Complexity: O(n^2), 
    The depth of the BFS is at most 4 by the four-square theorem (every natural number can be represented as the sum of four integer squares)
    At every depth there will be at most sqrt(n) children, because there's at most sqrt(n) perfect squares that are smaller than n
    (sqrt(n))^4 = n²
Space Complexity: O(n^2), 

@author: bohan

"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 1
        
        listPS = []
        
        i = 1
        while i*i <= n:
            listPS.append(i*i)
            i+=1
        
        if listPS[-1]**2 == n:
            return 1
        
        count = 0
        q = [n]
        
        while q:
            count += 1
            temp = []
            for curr in q:
                
                for ps in listPS:
                    if curr - ps == 0:
                        return count
                    elif curr - ps > 0:
                        temp.append(curr - ps)
            q = temp
        
        return count
        
        
        
            
        
        
        
        
        